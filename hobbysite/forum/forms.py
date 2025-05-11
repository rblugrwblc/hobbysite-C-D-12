from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    author_field = forms.CharField(label='Author', disabled=True, required=False)
    created_on_field = forms.DateTimeField(label='Created On', disabled=True, required=False)
    updated_on_field = forms.DateTimeField(label='Last Updated', disabled=True, required=False)

    class Meta:
        model = Thread
        fields = ['title', 'author_field', 'category', 'entry', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
