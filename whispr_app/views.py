from django.http.response import HttpResponse
from social.models import Post
from typing import ContextManager
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from profiles.models import Profile
from social.forms import CreatePostForm


class SignUpView(FormView):
    """
    Default View when not logged in to the application.
    Allows user to sign up
    or
    Allows user to Log in to app
    """

    template_name = 'sign_in_page.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def get(self, request):
        """
        If the user is logged in, redirect to the home page
        """
        if request.user.is_authenticated:
            return redirect(reverse_lazy('home'))

        # Otherwise go to sign in page
        return super().get(request)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

    def form_valid(self, form):
        """
        Called when form is valid and a new User object is to be created
        """
        # Call base implemetation to save user object
        response = super().form_valid(form)

        # Grabbing user to work with before success redirect
        user = form.instance
        user.save()
        Profile.objects.create(user=user)

        login(self.request, user)

        return response


class HomeView(TemplateView):
    """
    Main App Page
    """

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['post_form'] = CreatePostForm()
        return context

    def get(self, request):
        return super().get(request)

    def post(self, request):
        create_form = CreatePostForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
        
        return redirect(reverse_lazy('home'))
