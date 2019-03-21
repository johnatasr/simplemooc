from django.urls import path, include , re_path
from . import views
app_name = 'courses'

urlpatterns = [

    path('', views.index, name='index'),
    #path('<int:pk>', views.details, name='details'),
    #re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    #re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
    path('<slug>/', views.details, name='details'),
    ]
