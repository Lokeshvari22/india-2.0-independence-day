from django.db import models


class Question(models.Model):

    question = models.CharField(max_length=300)

    option_a = models.CharField(max_length=200)

    option_b = models.CharField(max_length=200)

    option_c = models.CharField(max_length=200)

    option_d = models.CharField(max_length=200)

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ("A", "Option A"),
            ("B", "Option B"),
            ("C", "Option C"),
            ("D", "Option D"),
        ]
    )

    explanation = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.question