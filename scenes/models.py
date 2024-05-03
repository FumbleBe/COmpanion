from django.db import models


class Image(models.Model):
    name = models.CharField()
    upload = models.ImageField()


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    image = models.ImageField(
        null=True,
        blank=True,
    )
    pj = models.ManyToManyField(to="actors.Character")
    starting_date = models.DateField()
    ending_date = models.DateField(blank=True, null=True)
    next_session = models.DateTimeField(blank=True, null=True)
    last_session = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        related_name="chapters",
        null=True,
        blank=True,
    )
    name = models.CharField()

    def __str__(self):
        return self.name


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
    chapter = models.ForeignKey(
        Chapter,
        on_delete=models.CASCADE,
        related_name="scenes",
        null=True,
        blank=True,
    )
    order = models.SmallIntegerField(default=0)
    image = models.ManyToManyField(
        to=Image,
        null=True,
        blank=True,
    )

    # def __str__(self):
    #     return "{}-{}-{}".format(self.campaign, self.chapter, self.title)
    def __str__(self):
        return self.title


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

    def __str__(self):
        return self.title
