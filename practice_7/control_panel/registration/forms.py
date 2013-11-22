from django import forms
from django.contrib import auth


class RegistrationForm(forms.Form):
    login_field = forms.CharField(label='login', max_length=20)
    password_field = forms.CharField(label='password', widget=forms.PasswordInput())
    retyped_password_field = forms.CharField(label='retyped password', widget=forms.PasswordInput())

    def clean(self):
        if self.cleaned_data.get('password_field') != self.cleaned_data.get('retyped_password_field'):
            raise forms.ValidationError('Passwords should be the same. Please, enter psswords again.')
        return self.cleaned_data


class AuthenticationForm(forms.Form):
    login_field = forms.CharField(label='login', max_length=20)
    password_field = forms.CharField(label='password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(AuthenticationForm, self).clean()
        if not self.errors:
            user = auth.authenticate(username=cleaned_data['login_field'], password=cleaned_data['password_field'])
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user
