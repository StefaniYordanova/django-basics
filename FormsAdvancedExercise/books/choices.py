from django.db import models


class Genres(models.TextChoices):
    FICTION = 'Fiction', 'Fiction'
    NON_FICTION = 'Non-Fiction', 'Non-Fiction'
    FANTASY = 'Fantasy', 'Fantasy'
    SCIENCE = 'Science', 'Science'
    ROMANCE = 'Romance', 'Romance'

class Languages(models.TextChoices):
    BULGARIAN = 'BG', 'Bulgarian'
    ENGLISH = 'EN', 'English'
    FRENCH = 'FR', 'French'
    GERMAN = 'GR', 'German'
    OTHER = 'Other', 'Other'
