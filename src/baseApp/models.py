from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class ContactPage(models.Model):
    title = models.CharField(max_length=100)
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    description = models.CharField(max_length=2000)