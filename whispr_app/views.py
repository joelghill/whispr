from django.shortcuts import render
from django.contrib.auth.views import LoginView 

class StartView(LoginView):

    template_name = 'login_page.html'

