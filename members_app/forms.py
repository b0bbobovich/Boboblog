from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models
from django import forms as basic_forms


class SignUpForm(auth_forms.UserCreationForm):
    email = basic_forms.EmailField(widget=basic_forms.EmailInput(attrs={"class": 'form-control'}))
    first_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    last_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))

    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(auth_forms.UserChangeForm):
    username = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    first_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    last_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    email = basic_forms.EmailField(widget=basic_forms.EmailInput(attrs={"class": 'form-control'}))

    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class PasswordChangingForm(auth_forms.PasswordChangeForm):
    old_password = basic_forms.CharField(widget=basic_forms.PasswordInput(attrs={"class": 'form-control', 'type': 'password'}))
    new_password1 = basic_forms.CharField(max_length=100, widget=basic_forms.PasswordInput(attrs={"class": 'form-control', 'type': 'password'}))
    new_password2 = basic_forms.CharField(max_length=100, widget=basic_forms.PasswordInput(attrs={"class": 'form-control', 'type': 'password'}))

    class Meta:
        model = auth_models.User
        fields = ('old_password', 'new_password1', 'new_password2')