from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from rules.choices import Source
from rules.models import Path


class Profile(models.Model):

    name = models.CharField(max_length=255)
    img = models.ImageField()
    slug = models.SlugField()
    description = models.TextField(blank=False)
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="profiles",
        null=True,
        blank=True,
    )
    dv = models.CharField(max_length=4)
    spellcasting = models.CharField(max_length=3)
    mpfactor = models.PositiveSmallIntegerField(default=0)
    paths = models.ManyToManyField(Path)
    prestige = models.BooleanField(default=False)
    equipment = models.ManyToManyField(to="items.Item", blank=True)

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        self.slug = slugify(self.name)
        if Profile.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            raise ValidationError(
                {
                    "name": [
                        "Ce profil existe déjà !",
                    ]
                }
            )
