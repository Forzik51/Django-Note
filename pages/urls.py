# Import the path and include functions from django.urls
from django.urls import path, include

# Import views from the current application
from . import views

# Define the URL patterns for the application
urlpatterns = [
    # URL pattern for the home page
    path('', views.home, name="home"),

    # URL pattern for the note page
    path('note', views.note, name="note"),

    # URL pattern for the register/login page
    path('register_login/', views.register_login, name='register_login'),

    # URL pattern for logging out
    path('logout/', views.logout, name='logout'),

    # URL pattern for adding a note
    path('addNote/', views.add_note, name='addNote'),

    # URL pattern for deleting a note by ID
    path('deleteNote/<int:note_id>/', views.delete_note, name='deleteNote'),

    # URL pattern for selecting a note by ID
    path('selectNote/<int:note_id>/', views.select_note, name='selectNote'),

    # URL pattern for renaming a note by ID
    path('renameNote/<int:note_id>/', views.rename_note, name='renameNote'),
    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    # URL pattern for getting div text content via AJAX
    path('get-div-text/', views.get_div_text, name='get_div_text'),
]
