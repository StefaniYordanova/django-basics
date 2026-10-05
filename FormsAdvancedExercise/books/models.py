from django.db import models
from django.utils.text import slugify
from .validators import IsbnValidator
from .choices import Genres, Languages

# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=20,
        unique=True,
    )
    author = models.CharField(
        max_length=50,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    isbn = models.CharField(
        unique=True,
        validators=[
            IsbnValidator(),
        ],
    )
    genre = models.CharField(
        max_length=30,
        choices=Genres.choices,
        default=Genres.NON_FICTION,
    )
    language = models.CharField(
        max_length=10,
        choices=Languages.choices,
        default=Languages.OTHER,
    )
    pages = models.PositiveIntegerField()
    is_available = models.BooleanField(
        default=True,
    )
    publishing_date = models.DateField(
        auto_now_add=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField()
    slug = models.CharField(
        max_length=100,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.title}-{self.author}")
        super().save(*args, **kwargs)
