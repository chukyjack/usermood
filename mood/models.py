from django.conf import settings
from django.db import models


class Mood(models.Model):
    VERY_LOW = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    VERY_HIGH = 5

    mood_choices = (
        (VERY_LOW, 'Very Low'),
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (VERY_HIGH, 'Very High'),
    )
    mood = models.IntegerField(choices=mood_choices, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-created_date',)
