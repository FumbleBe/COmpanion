from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from rules.choices import Source
from rules.models import Path, Capacity


class Species(models.Model):

    name = models.CharField(max_length=255)
    img = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField(blank=False)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="species",
        null=True,
        blank=True,
    )
    STR = models.SmallIntegerField(default=0)
    DEX = models.SmallIntegerField(default=0)
    CON = models.SmallIntegerField(default=0)
    INT = models.SmallIntegerField(default=0)
    WIS = models.SmallIntegerField(default=0)
    CHA = models.SmallIntegerField(default=0)
    paths = models.ManyToManyField(Path)
    capacities = models.ManyToManyField(Capacity)

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        self.slug = slugify(self.name)
        if Species.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError(
                {
                    "name": [
                        "Cette race existe déjà !",
                    ]
                }
            )

    class Meta:
        verbose_name_plural = "Species"
        ordering = ['name']
