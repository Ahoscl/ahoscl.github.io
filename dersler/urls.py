from django.contrib import admin
from django.urls import path, include
from .views import index, kategoriolustur, dersolustur, kategoriler, kategori_ayrinti,ders_ayrinti

app_name = 'dersler'

urlpatterns = [
    path('', index, name='index'),
    path('yeni-kategori/', kategoriolustur, name='kategoriolustur'),
    path('yeni-ders/', dersolustur, name='dersolustur'),
    path('kategoriler/', kategoriler, name='kategoriler'),
    path('kategori/<int:kategori_id>', kategori_ayrinti, name='kategori_ayrinti'),
    path('ders/<int:ders_id>', ders_ayrinti, name='ders_ayrinti'),

]
