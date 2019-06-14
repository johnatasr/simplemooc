from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views



app_name = 'core'
app_name = 'courses'
app_name = 'accounts'


urlpatterns = [
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registrar/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dash'),
   ]
