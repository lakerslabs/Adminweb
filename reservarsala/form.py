from django import forms
from .models import reservaSala

class reservaForm(forms.ModelForm):
    class Meta:
        model = reservaSala
        fields = '__all__'