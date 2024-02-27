from django.db import models
from rules.models import SOURCE_CHOICES, Capacity


class Path(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    img = models.ImageField()
    description = models.TextField(blank=False)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    capacities = models.ManyToManyField(Capacity)
    prestige = models.BooleanField(default=False)
    racial = models.BooleanField(default=False)
    encounter = models.BooleanField(default=False)

    def __str__(self):
        return self.name
