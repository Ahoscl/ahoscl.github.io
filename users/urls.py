from django.contrib import admin
from django.urls import path, include
from .views import register, profile, editprofile

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:user_id>', profile, name='profile'),
    path('editprofile/', editprofile, name='editprofile')

]
