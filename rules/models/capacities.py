from django.db import models
from rules.models import SOURCE_CHOICES

class Capacity(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=False)
    source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    spell = models.BooleanField(default=False)
    limited = models.BooleanField(default=False)
    encounter = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = "Capacities"
