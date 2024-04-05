from django.db import models
from rules.choices import Source
from django.utils.text import slugify
from django.core.exceptions import ValidationError

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

    def clean_fields(self, exclude=None):
        self.slug = slugify(self.name)
        if Capacity.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError(
                {
                    "name": [
                        "Cette capacité existe déjà !",
                    ]
                }
            )

    class Meta:
        verbose_name_plural = "Capacities"
