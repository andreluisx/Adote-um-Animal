from typing import Any
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You have not provide a valid e-mail address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extrafields):
        extrafields.setdefault('is_staff', False)
        extrafields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extrafields)
    
    def create_superuser(self, email=None, password=None, **extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extrafields)
    
class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    cpf=models.CharField(max_length=11)
    number = models.IntegerField(validators=[
            MaxValueValidator(100000000000),
            MinValueValidator(10)
        ])
    cidade = models.CharField(max_length=225)
    estado = models.CharField(max_length=2)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta():
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name
    
    def get_full_name(self):
        return self.name or self.email.split('@')[0]