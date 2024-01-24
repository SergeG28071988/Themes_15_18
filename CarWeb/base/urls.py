from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [   
    path('', views.auto_list, name='auto_list'),    
    path('add_auto', views.add_auto, name='add_auto'),
    path('about-us', views.about, name='about'),
]
