from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


class loginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)
