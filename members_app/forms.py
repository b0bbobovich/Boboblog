from django.contrib.auth import forms as auth_forms
from django.contrib.auth import models as auth_models
from django import forms as basic_forms
from main_app import models as main_app_models


class SignUpForm(auth_forms.UserCreationForm):
    email = basic_forms.EmailField(widget=basic_forms.EmailInput(attrs={"class": 'form-control'}))
    first_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    last_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))

    class Meta:
        model = auth_models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EntireProfileForm(basic_forms.ModelForm):
    class Meta:
        model = main_app_models.UserProfile
        fields = ['bio', 'profile_pics', 'website_url', 'facebook_url', 'instagram_url', 'linkedin_url']

        widgets = {
            'bio': basic_forms.Textarea(attrs={"class": 'form-control'}),
            'website_url': basic_forms.URLInput(attrs={"class": 'form-control'}),
            'facebook_url': basic_forms.URLInput(attrs={"class": 'form-control'}),
            'instagram_url': basic_forms.URLInput(attrs={"class": 'form-control'}),
            'linkedin_url': basic_forms.URLInput(attrs={"class": 'form-control'})
        }


class AuthDataProfileForm(auth_forms.UserChangeForm):
    username = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    first_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    last_name = basic_forms.CharField(max_length=100, widget=basic_forms.TextInput(attrs={"class": 'form-control'}))
    email = basic_forms.EmailField(widget=basic_forms.EmailInput(attrs={"class": 'form-control'}))

    class Meta:
        model = auth_models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', ]
#
#
#class UsersDataProfileForm(basic_forms.ModelForm):
#    bio = basic_forms.CharField(widget=basic_forms.Textarea(attrs={"class": 'form-control'}))
#    website_url = basic_forms.URLField(max_length=100, widget=basic_forms.URLInput(attrs={"class": 'form-control'}))
#    facebook_url = basic_forms.URLField(max_length=100, widget=basic_forms.URLInput(attrs={"class": 'form-control'}))
#    instagram_url = basic_forms.URLField(max_length=100, widget=basic_forms.URLInput(attrs={"class": 'form-control'}))
#    linkedin_url = basic_forms.URLField(max_length=100, widget=basic_forms.URLInput(attrs={"class": 'form-control'}))
#
#
#    class Meta:
#        model = main_app_models.UserProfile
#        fields = ['bio', 'website_url', 'facebook_url', 'instagram_url', 'linkedin_url', 'profile_pics']
#
#
#class EntireProfileForm(AuthDataProfileForm, UsersDataProfileForm):
#    pass



class PasswordChangingForm(auth_forms.PasswordChangeForm):
    old_password = basic_forms.CharField(widget=basic_forms.PasswordInput(attrs={"class": 'form-control', 'type': 'password'}))
    new_password1 = basic_forms.CharField(max_length=100, widget=basic_forms.PasswordInput(attrs={"class": 'form-control', 'type': 'password'}))
    new_password2 = basic_forms.CharField(max_length=100, widget=basic_forms.PasswordInput(attrs={"class": 'form-control', 'type': 'password'}))

    class Meta:
        model = auth_models.User
        fields = ['old_password', 'new_password1', 'new_password2']


class ProfilePageForm(basic_forms.ModelForm):
    class Meta:
        model = main_app_models.UserProfile
        fields = ('bio', 'profile_pics', 'website_url', 'facebook_url', 'instagram_url', 'linkedin_url')
        widgets = {
            'bio': basic_forms.Textarea(attrs={"class": 'form-control'}),
            'website_url': basic_forms.URLInput(attrs={"class": 'form-control'}),
            'facebook_url': basic_forms.URLInput(attrs={"class": 'form-control'}),
            'instagram_url': basic_forms.URLInput(attrs={"class": 'form-control'}),
            'linkedin_url': basic_forms.URLInput(attrs={"class": 'form-control'})
        }
