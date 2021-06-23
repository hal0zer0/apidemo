from django.db import models
from django.contrib.auth.models import User as BaseUser

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class User(BaseUser):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    birthdate = models.DateField()

    def __str__(self):
        return self.name