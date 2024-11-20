from django import forms
from .models import Sotuv

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sotuv
        fields = ['mahsulot', 'miqdori','jami_narxi']
        read_only_fields = ['jami_narxi']

    def clean_quantity(self):
        miqdori = self.cleaned_data['miqdori']
        if miqdori <= 0:
            raise forms.ValidationError("Soni ijobiy bo'lishi kerak.")
        return miqdori
