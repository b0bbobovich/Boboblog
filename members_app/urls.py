from django.urls import path
from . import views as my_views

urlpatterns = [
    path('register/', my_views.UserRegister.as_view(), name='register'),
    path('edit_profile/', my_views.UserEdit.as_view(), name='edit-profile'),
   #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', my_views.PasswordsChange.as_view(template_name='registration/change-password.html')),
    path('password_success/', my_views.password_success, name='password-success'),
    ]