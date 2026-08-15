from django.db import models


class HistoricalEvent(models.Model):

    year = models.IntegerField()

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    image_url = models.URLField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["year"]

    def __str__(self):
        return f"{self.year} - {self.title}"