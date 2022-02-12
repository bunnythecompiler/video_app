"""video_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from streamers import views as streamers_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stream.urls')),
    path('profile',streamers_views.profile, name="profile"),
    path('register/',streamers_views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='streamers/login.html'), name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name='streamers/logout.html'), name="logout"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

