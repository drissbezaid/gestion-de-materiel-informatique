from django import forms
from .models import Materiel

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = '__all__'
        widgets = {
            'date_achat': forms.DateInput(attrs={'type': 'date'})
        }