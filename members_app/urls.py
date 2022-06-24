from django.urls import path
from . import views as my_views

urlpatterns = [
    path('register/', my_views.UserRegister.as_view(), name='register'),
    path('edit_profile/', my_views.UserEdit.as_view(), name='edit-profile'),
   #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', my_views.PasswordsChange.as_view(template_name='registration/change-password.html')),
    path('password_success/', my_views.PasswordsChange.password_success, name='password-success'),
    path('<int:pk>/profile/', my_views.ShowProfilePage.as_view(), name='show-profile-page'),
    path('<int:pk>/edit_profile_page/', my_views.EditProfilePage.as_view(), name='edit-profile-page'),
    path('create_profile_page/', my_views.CreateProfilePage.as_view(), name='create-profile-page'),
    ]