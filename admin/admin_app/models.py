from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

# Create your models here.
class Messages(models.Model):
    message = models.CharField(max_length=255)

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text= ('This is the group a user belongs to and gets the permissions of that group.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        related_query_name='user',
        help_text=('Specific permissions of a user')
    )
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)