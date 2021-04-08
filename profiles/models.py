from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    bio = models.CharField(max_length=400, blank=True, default='')
    following = models.ManyToManyField(to='profiles.Profile', related_name='followers', blank=True, null=True)

    def __str__(self):
        return self.user.username

