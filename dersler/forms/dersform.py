from ..models import DersModel
from django import forms


class DersForm(forms.ModelForm):
    class Meta:
        model = DersModel
        fields = '__all__'
