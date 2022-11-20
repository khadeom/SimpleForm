
from django.contrib import admin
from django.urls import path, include
from .views import incident

urlpatterns = [
    
    path("", incident, name = 'incident')
]
