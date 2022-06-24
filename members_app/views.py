from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth import models as auth_models
from . import forms as my_forms
from main_app import models as main_app_models


class UserRegister(CreateView):
    form_class = my_forms.SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEdit(UpdateView):
    form_class = my_forms.AuthDataProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChange(auth_views.PasswordChangeView):
    form_class = my_forms.PasswordChangingForm
    success_url = reverse_lazy('password-success')

    def password_success(request):
        return render(request, 'registration/password_success.html', {})


class ShowProfilePage(DetailView):
    model = main_app_models.UserProfile
    form_class = my_forms.EntireProfileForm
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)

        user_profile_data = get_object_or_404(main_app_models.UserProfile, id=self.kwargs['pk'])

        context['user_profile_data'] = user_profile_data
        return context


class EditProfilePage(UpdateView):
    model = main_app_models.UserProfile
    form_class = my_forms.ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')


class CreateProfilePage(CreateView):
    model = main_app_models.UserProfile
    form_class = my_forms.ProfilePageForm
    template_name = 'registration/create_profile_page.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
