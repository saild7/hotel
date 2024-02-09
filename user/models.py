from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=10)
    address = models.CharField(blank=True, max_length=150)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '
