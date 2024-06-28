# Import modules from Django
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

# from PPY_proj.settings import EMAIL_HOST_USER
from pages.models import Note


def home(request):
    return render(request, 'pages/log_in_main.html')


# View to handle user logout
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect(home)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('note')
    else:
        return redirect(request, 'home')


# View to handle user registration and login
def register_login(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return redirect('home')

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email exist')
                return redirect('home')

            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            user.is_active = True
            user.save()

            # urrent_site = get_current_site(request)
            # mail_subject = 'Activate your account.'
            # message = render_to_string('pages/email_verification.html', {
            #    'user': user,
            #    'domain': current_site.domain,
            #    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #    'token': default_token_generator.make_token(user),
            # })
            # send_mail(mail_subject, "hkjhkunlnlnlm;m;m", EMAIL_HOST_USER, [email], fail_silently=False)
            return redirect(home)  # Redirect to a success page

        elif 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                # if user.is_active:
                auth.login(request, user)
                return redirect(note)  # Redirect to home page
            else:
                # Handle invalid login
                return redirect(home)

    else:
        return render(request, home)


# View to display nav notes for the logged-in user
def note(request):
    user_note = Note.objects.filter(userId=request.user.id)

    context = {
        "notes": user_note,
    }
    return render(request, "pages/main.html", context)


# View to add a new note
def add_note(request):
    note_add = Note.objects.create(userId=request.user, noteName="", noteText="")
    note_add.save()
    return redirect(note)


# View to delete a note by ID
def delete_note(request,  note_id):
    product = get_object_or_404(Note, id=note_id)
    product.delete()
    return redirect(note)


# View to select a note by ID and display nav
def select_note(request, note_id):
    user_select_note = get_object_or_404(Note, userId=request.user.id, id=note_id)
    user_note = Note.objects.filter(userId=request.user.id)
    context = {
        "note": user_select_note,
        "notes": user_note,
    }
    return render(request, "pages/main.html", context)


# View to handle AJAX request to update note text
def get_div_text(request):
    if request.method == 'POST':
        div_text = request.POST.get('div_text', '')
        object_id = request.POST.get('object_id', None)
        note_update = get_object_or_404(Note, id=object_id)
        note_update.noteText = div_text
        note_update.save()
        response_data = {'message': 'Text received', 'div_text': div_text}
        return JsonResponse(response_data)
    return JsonResponse({'message': 'Invalid request'}, status=400)


# View to rename a note by ID
def rename_note(request, note_id):
    if request.method == 'POST':
        name = request.POST.get('renameInput')
        note_update = get_object_or_404(Note, id=note_id)
        note_update.noteName = name
        note_update.save()

    return redirect(note)
