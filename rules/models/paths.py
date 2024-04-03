from django.db import models
from rules.choices import Source
from rules.models import Capacity


class Path(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    img = models.ImageField()
    description = models.TextField(blank=False)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="paths",
        null=True,
        blank=True,
    )
    capacities = models.ManyToManyField(Capacity)
    prestige = models.BooleanField(default=False)
    racial = models.BooleanField(default=False)
    encounter = models.BooleanField(default=False)

    def __str__(self):
        return self.name
