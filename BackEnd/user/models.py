from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin
from django.db import models
import uuid

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('El email es un campo requerido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuario necesita tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super usuario necesita is_superuser=True')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES =(
        ('client', 'Client'),
        ('admin', 'Admin'),
    )
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_email_confirmed = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    objects = CustomUserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['first_name','last_name','user_type']

    def __strt__(self):
        return self.email