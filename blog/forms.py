from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    A Django form for creating and updating Comments.
    """
    class Meta:
        model = Comment
        fields = ('body',)
