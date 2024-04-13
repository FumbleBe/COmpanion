from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from rules.choices import Source
from rules.models import Capacity


class Path(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    img = models.ImageField(blank=True, null=True)
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

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
            if Path.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                raise ValidationError(
                    {
                        "name": [
                            "La voie '{}' existe déjà !".format(self.name),
                        ]
                    }
                )
        super(Path, self).save(*args, **kwargs)
