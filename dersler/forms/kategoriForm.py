from ..models import KategoriModel
from django import forms


class KategoriForm(forms.ModelForm):
    class Meta:
        model = KategoriModel
        fields = '__all__'
