from django import forms
from .models import Review
from FormsAdvancedExercise.mixins import DisabledFormFieldsMixin


class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

class ReviewCreateForm(ReviewBaseForm):
    class Meta(ReviewBaseForm.Meta):
        exclude = ['book']

class ReviewDeleteForm(DisabledFormFieldsMixin, ReviewBaseForm):
    ...
