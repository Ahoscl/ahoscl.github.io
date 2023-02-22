from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserCreationFormMe(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationFormMe, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserChangeFormMe(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserChangeFormMe, self).save(commit=False)
        if commit:
            user.save()
        return user
