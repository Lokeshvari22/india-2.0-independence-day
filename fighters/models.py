from django.db import models


class FreedomFighter(models.Model):

    name = models.CharField(max_length=200)

    birth_year = models.IntegerField()

    death_year = models.IntegerField(
        blank=True,
        null=True
    )

    short_description = models.CharField(
        max_length=300
    )

    biography = models.TextField()

    contribution = models.TextField()

    image_url = models.URLField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name