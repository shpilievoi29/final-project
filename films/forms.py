from django.core.exceptions import ValidationError
from django import forms

from films.models import Film


class ReviewForms(forms.Form):
    review = forms.CharField(label="Film review")
    rate = forms.IntegerField(label="Film rate", max_value=5, min_value=1)
    film = forms.ModelChoiceField(required=False, queryset=Film.objects.all())

    def clean_review(self):
        review = self.cleaned_data.get("review")
        if not review:
            raise ValidationError("review text required")
        else:
            return review

    def clean_rate(self):
        rate = self.cleaned_data.get("rate")
        if rate < 1 or rate > 5:
            raise ValidationError("rate should be between 1 or 5")

    def clean(self):
        super().clean()
