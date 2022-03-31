from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class User(models.Model):
    # Can add more school attributes (e.g. public/private, location, ranking) later on
    name = models.CharField(max_length=128, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Tag(models.Model):
    # Can add more school attributes (e.g. public/private, location, ranking) later on
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
