from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%Y-%m-%d'])
