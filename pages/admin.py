# Import the admin module
from django.contrib import admin

# Import the Note model
from pages.models import Note


# Define the admin configuration
class NoteAdmin(admin.ModelAdmin):
    # Display the id and noteName fields in the list view
    list_display = ('id', 'noteName')

    # Make the id and noteName fields clickable links
    list_display_links = ('id', 'noteName')

    # Limit the number of notes displayed per page
    list_per_page = 30

# Register the Note model
admin.site.register(Note, NoteAdmin)
