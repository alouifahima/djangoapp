import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Machine_virtuelle(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type_OS = models.CharField(max_length=200)
    version_OS = models.CharField(max_length=200)
    hard_disk_size = models.FloatField(default=0)
    ram = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Abonnement(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    type_Abonnement = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    date_joind = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user)
