from django.shortcuts import render
from django.views.generic.edit import FormView
from social.models import Post

class PostCreateView(Form):
    """

    """
    model = Post
    fields = ['content']
