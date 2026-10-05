from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class IsbnValidator:
    DEFAULT_MESSAGE = "The isbn must contain exactly 13 characters!"

    def __init__(self, message: str = DEFAULT_MESSAGE) -> None:
        self.message = message

    def __call__(self, value: str) -> ValidationError | None:
        if len(value) != 13:
            raise ValidationError(self.message)

