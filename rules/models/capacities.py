from django.db import models


class Capacity(models.Model):
    SOURCE_CHOICES = [("",""),("drs", "CO DRS"), ("compagnon", "CO Compagnon"), ("5E", "D&D 5E"), ("homebrew","Règle Maison")]

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=False)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    spell = models.BooleanField(default=False)
    limited = models.BooleanField(default=False)
