from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class AppointmentsList(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    problem = models.CharField(max_length=100, null=False)
    details = models.TextField(null=True, blank=True)
    draft_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    updation_time = models.DateTimeField(auto_now=True)

    def getEditURL(self):
        return "/appointments/{self.id}/Edit"

    def getDeleteURL(self):
        return "/appointments/{self.id}/Delete"
