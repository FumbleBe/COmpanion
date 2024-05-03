from django.db import models


class Image(models.Model):
    name = models.CharField()
    upload = models.ImageField()


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        related_name="campaigns",
        null=True,
        blank=True,
    )
    pj = models.ManyToManyField(to="actors.Character")
    starting_date = models.DateField()
    ending_date = models.DateField(blank=True, null= True)
    next_session = models.DateTimeField(blank=True, null= True)
    last_session = models.DateField(blank=True, null=True)


class Scene(models.Model):
    title = models.CharField()
    description = models.TextField()
    npc = models.ForeignKey(
        "actors.NPC",
        on_delete=models.CASCADE,
        related_name="scenes",
        null=True,
        blank=True,
    )
    encounter = models.ForeignKey(
        "actors.Encounter",
        on_delete=models.CASCADE,
        related_name="scenes",
        null=True,
        blank=True,
    )
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="scenes",
        null=True,
        blank=True,
    )
    image = models.ManyToManyField(to=Image)

class Session(models.Model):
    scene = models.ForeignKey(
        Scene,
        on_delete=models.CASCADE,
        related_name="sessions",
        null=True,
        blank=True,
    )
    date = models.DateField()
    title = models.CharField(max_length=100)
    summary = models.TextField()
