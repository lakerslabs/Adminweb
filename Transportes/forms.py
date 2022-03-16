from django import forms
# from django.db.models import fields
from .models import Transporte

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'
        # widgets = {
        #     'COD_TRANSP': forms.TextInput(attrs={'class':'form-control'}),
        #     'NOMBRE': forms.TextInput(attrs={'class':'form-control'}),
        #     'COSTE_BULTO': forms.NumberInput(attrs={'class':'form-control'}),
        #     'COSTE_SEGURO': forms.NumberInput(attrs={'class':'form-control'}),
        #     'COSTE_RETIRO': forms.NumberInput(attrs={'class':'form-control'}),
        #     'COSTE_ENTREGA': forms.NumberInput(attrs={'class':'form-control'}),
        #     'RETIRA_EN_CD': forms.CheckboxInput(attrs={'class':'form-control'}),
        #     'OBSERVASIONES': forms.TextInput(attrs={'class':'form-control'}),
        # }
        