from django.db import models
from profiles.models import Profile

class Post(models.Model):
    content = models.TextField(max_length=280, blank=False, default='')
    author = models.ForeignKey(to=Profile, related_name='posts', on_delete=models.CASCADE)
