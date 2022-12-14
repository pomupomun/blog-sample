from dataclasses import field, fields
from socket import fromshare
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","email","body"]