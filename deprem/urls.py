from django.contrib import admin
from django.urls import path, include
from .views import index

app_name = 'deprem'

urlpatterns = [
    path('', index, name='index'),
]
