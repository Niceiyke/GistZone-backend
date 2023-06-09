from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class myUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username=models.CharField(max_length=20)
    first_name =models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    rank= models.PositiveIntegerField(default=0,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_veryfied = models.BooleanField(default=False)
    is_banned= models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def get_full_name (self):
        return f'{str(self.first_name)} {str(self.last_name)}'

