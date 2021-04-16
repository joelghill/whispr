from django.db import models
from profiles.models import Profile

class Post(models.Model):
    """ Model represeting a user's post in the social network
    """
    content = models.TextField(max_length=280, blank=False, default='')
    author = models.ForeignKey(to=Profile, related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
