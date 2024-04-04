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


class ItemSubtypeChoice(models.TextChoices):
    OTHER = "other", "Divers"
    ARMOR = "armor", "Armure"
    SHIELD = "shield", "Bouclier"
    MELEE = "melee", "Arme de contact"
    RANGED = "ranged", "Arme à distance"
    SPELL = "spell", "Sort"
    JEWEL = "jewel", "Bijou"
    SCROLL = "scroll", "Parchemin"
    WAND = "wand", "Baguette"
    AMMUNITION = "ammunition", "Munition"
    CONSUMABLE = "consumable", "Consommable"
    CONTAINER = "container", "Contenant"
    MOUNT = "mount", "Monture"
    CURRENCY = "currency", "Monnaie"
    EQUIPMENT = "equipment", "Equipement"


class ItemTrait(models.Model):
    """
    Équipement
    Arme
    Protection
    À distance
    Effet magique
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class AttackChoice(models.TextChoices):
    MELEE = "melee", "Attaque de Contact"
    RANGED = "ranged", "Attaque à Distance"
    MAGIC = "magic" "Attaque Magique"


class SlotChoice(models.TextChoices):
    HAND = "hand", "Main"
    HEAD = "head", "Tête"
    EAR = "ear", "Oreille"
    NECK = "neck", "Cou"
    SHOULDERS = "shoulders", "Épaules"
    CHEST = "chest", "Torse"
    BACK = "back", "Dos"
    ARM = "arm", "Bras"
    FINGER = "finger", "Doigt"
    WRIST = "wrist", "Poignet"
    WAIST = "waist", "Taille"
    LEGS = "legs", "Jambes"
    FEET = "feet", "Pieds"
    BELT = "belt", "À la ceinture"
    BACKPACK = "backpack", "Sac-à-dos"
    QUIVER = "quiver", "Carquois"


class ReloadChoice(models.TextChoices):
    NOACTION = "noaction", "Pas d'action"
    SIMPLE = "simple", "Action simple (S)"
    LIMITED = "limited", "Action limitée (L)"
