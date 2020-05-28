from django.db import models


# Create your models here.
class CreateNewUser(models.Model):
    fname = models.CharField(max_length=50, null=False,)
    lname = models.Charfield(max_length=50, null=False,)
    username = models.Charfield(max_length=50, null=False,)
    email = models.Charfield(max_length=50, null=False,)