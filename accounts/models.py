from django.db import models
from django import forms
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.forms import widgets, Widget

GENDER_CHOICES = (('M', 'Male'),('F', 'Female'))
CITY_CHOICES = (('T','Tunis'),('N','Nabeul'),('A','Ariana'))

class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, date_of_birth, phone_number, gender, city, address, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            phone_number = phone_number,
            gender = gender,
            city = city,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth, phone_number, gender, city, address, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name = last_name,
            date_of_birth=date_of_birth,
            phone_number= phone_number,
            gender = gender,
            city = city,
            address=address,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.DecimalField(max_digits=8,decimal_places=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    city = models.CharField(choices=CITY_CHOICES, max_length=128)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'date_of_birth', 'phone_number', 'gender', 'city', 'address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
