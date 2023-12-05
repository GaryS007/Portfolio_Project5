from django import forms
from .models import Reviews
from .widgets import CustomClearableFileInput


class ReviewsForm(forms.ModelForm):
    """ Creates the reviews form """

    class Meta:
        model = Reviews
        fields = ("review_title", "review_rating", "review_text")
    
    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
