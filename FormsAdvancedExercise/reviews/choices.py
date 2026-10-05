from django.db import models

class ReviewTypes(models.TextChoices):
    TEXT = 'Text', 'Text'
    AUDIO = 'Audio', 'Audio'
    VIDEO = 'Video', 'Video'
