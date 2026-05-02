"""Defines database models for the notes app."""

from django.db import models


class Note(models.Model):
    """Represents a single user-created note with a title and content."""
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        """Returns string representation of the note."""
        return self.title
