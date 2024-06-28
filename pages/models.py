# Import the User model from django.contrib.auth.models to associate notes with users
from django.contrib.auth.models import User

# Import the models module from django.db to create model fields and relationships
from django.db import models


# Define the Note model
class Note(models.Model):
    # Foreign key relationship to the User model, with cascade delete
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    # Text field for the content of the note
    noteText = models.TextField(blank=True)

    # Text field for the name
    noteName = models.TextField(blank=True)

    # String representation of the Note model
    def __str__(self):
        return f" {self.noteText} {self.noteName} "
