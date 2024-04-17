from django.db import models
from rules.choices import Source
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class AbstractCapacity(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=False, null=True)
    # source = models.ForeignKey(
    #     Source,
    #     on_delete=models.PROTECT,
    #     related_name="capacities",
    #     null=True,
    #     blank=True,
    # )
    spell = models.BooleanField(default=False)
    limited = models.BooleanField(default=False)
    encounter = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

    class Meta:
        abstract = True


class Capacity(AbstractCapacity):
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="capacities",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
            if Capacity.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                raise ValidationError(
                    {
                        "name": [
                            "La capacité {} existe déjà !".format(self.name),
                        ]
                    }
                )
        super(Capacity, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Capacities"
