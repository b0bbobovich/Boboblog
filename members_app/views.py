from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from . import forms as my_forms

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegister(CreateView):
    form_class = my_forms.SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(UpdateView):
    form_class = my_forms.EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChange(auth_views.PasswordChangeView):
    form_class = my_forms.PasswordChangingForm
    success_url = reverse_lazy('password-success')
