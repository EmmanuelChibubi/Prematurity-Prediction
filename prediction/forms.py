from django import forms
from .models import PredictionData

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionData
        fields = ['input_data']
