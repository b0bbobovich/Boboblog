from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('members_app/', include('django.contrib.auth.urls')),
    path('', include('members_app.urls')),
]
