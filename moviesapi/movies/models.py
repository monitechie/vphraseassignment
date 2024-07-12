from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    movies = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    oneline = models.TextField(blank=True)
    stars = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    runtime = models.FloatField()
    gross = models.FloatField(default=0)

    def __str__(self):
        return self.title
