from django.forms import ModelForm
from .models import MoviePickerModel
from django import forms


class MoviePickerForm(ModelForm):
    class Meta:
        model = MoviePickerModel
        fields = ['Name', 'Title', 'Rate', 'Review']

        widgets = {}

