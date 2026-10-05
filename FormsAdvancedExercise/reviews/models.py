from django.db import models
from .choices import ReviewTypes


# Create your models here.
class Review(models.Model):
    author = models.CharField(
        max_length=50,
    )
    body = models.TextField(
        null=True,
        blank=True,
    )
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    is_verified = models.BooleanField(
        default=True,
    )
    review_type = models.CharField(
        max_length=30,
        choices=ReviewTypes.choices,
        default=ReviewTypes.TEXT,
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    book = models.ForeignKey(
        to='books.Book',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
