from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

GENRES = (
    (-1, 'not defined'),
    (0, 'rock'),
    (1, 'metal'),
    (2, 'pop'),
    (3, 'hip-hop'),
    (4, 'electronic'),
    (5, 'reggae'),
    (6, 'other'),
)

class Genre(models.Model):
    name = models.CharField(max_length=32, blank=False)

class Person(models.Model):
    first_name = models.CharField(max_length=32, blank=True, default="")
    last_name  = models.CharField(max_length=32, blank=False)

class Movie(models.Model):
    title       = models.CharField(max_length=128, blank=False)
    director    = models.ForeignKey(Person,null=True, default="", on_delete=models.SET_NULL)
    year        = models.IntegerField(null=True)
    rating      = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    genres      = models.ManyToManyField(Genre, null=True)

"""
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name  = models.CharField(max_length=32)

class Movie(models.Model):
    title       = models.CharField(max_length=128)
    screenplay  = models.CharField(max_length=128, blank=True, default="")
    starring    = models.CharField(max_length=128, blank=True, default="")

class PersonMovie(models.Model):
    StarRole    = models.CharField(max_length=32)

class StarRole(models.Model):
    name = models.CharField(max_length=32)
"""