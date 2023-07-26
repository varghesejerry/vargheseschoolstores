# forms.py

from django import forms
from .models import materials

class MaterialForm(forms.ModelForm):
    class Meta:
        model = materials
        fields = ['name']
