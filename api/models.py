from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from gettext import gettext as _

# Create your models here.
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user



class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
    organization = models.ForeignKey('Organization', related_name='users', on_delete=models.CASCADE, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.name

