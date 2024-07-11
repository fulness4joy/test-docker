from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='avatars/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Измените related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Измените related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    def __str__(self):
        return self.username