from django.contrib import admin
from django.urls import path, include
from . views import home, contact
app_name = 'core'



urlpatterns = [

    path('', home, name='home'),
    path('contato/', contact, name='contact'),


]
