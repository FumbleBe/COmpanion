from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class CaracChoice(models.TextChoices):
    STR = "STR", "Force"
    DEX = "DEX", "Dextérité"
    CON = "CON", "Constitution"
    INT = "INT", "Intelligence"
    WIS = "WIS", "Sagesse"
    CHA = "CHA", "Charisme"


class RarityChoice(models.TextChoices):
    COMMON = "common", "Commun"
    MODERATE = "moderate", "Modéré"
    RARE = "rare", "Rare"
    VERYRARE = "very-rare", "Très rare"
    UNIQUE = "unique", "Unique"


class SizeChoice(models.TextChoices):
    TINY = "tiny", "Minuscule"
    REALLYSMALL = "really_small", "Très petit"
    SMALL = "small", "Petit"
    MEDIUM = "medium", "Moyen"
    TALL = "tall", "Grand"
    HUGE = "huge", "Énorme"
    COLOSSAL = "colossal", "Colossale"

class GenderChoice(models.TextChoices):
    MALE = "male", "Homme"
    FEMALE = "female", "Femme"
