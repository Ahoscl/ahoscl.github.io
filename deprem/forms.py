from .models import Deprem
from django import forms


class KategoriForm(forms.ModelForm):
    class Meta:
        model = Deprem
        fields = '__all__'
