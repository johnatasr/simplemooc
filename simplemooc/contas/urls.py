from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'contas'
app_name = 'core'



urlpatterns = [
     path('entrar/', LoginView.as_view(template_name='contas/contas_login.html'),  name='login'),
     path('sair/', LogoutView.as_view(next_page='/'),  name='logout'),
     path('cadastre-se/', views.register, name='registro'),
]

