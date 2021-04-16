from django import forms
from django.forms import fields
from social.models import Post


class CreatePostForm(forms.ModelForm):
    """ Form for creating new posts
    """

    class Meta:
        model = Post
        fields = ['content', 'author']
