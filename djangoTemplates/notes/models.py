from datetime import date

from django.db import models

# Create your models here.

class Note(models.Model):
    class Priorities(models.TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'

    title = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    priority = models.CharField(
        max_length=10,
        choices=Priorities.choices,
        default=Priorities.LOW,
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    is_completed = models.BooleanField(
        default=False,
    )
    due_date = models.DateField(
        default=date.today,
    )
