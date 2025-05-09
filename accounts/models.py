from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    plaid_access_token = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"