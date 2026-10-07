from django import forms
from .models import Book
from FormsAdvancedExercise.mixins import DisabledFormFieldsMixin


class BaseBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['slug', ]

class BookCreateForm(BaseBookForm):
    ...

class BookDeleteForm(DisabledFormFieldsMixin, BaseBookForm):
    ...