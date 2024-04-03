from django.db import models
from rules.choices import Source

class Capacity(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=False)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="capacities",
        null=True,
        blank=True,
    )
    spell = models.BooleanField(default=False)
    limited = models.BooleanField(default=False)
    encounter = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = "Capacities"
