from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('analiz/', include('analiz.urls')),
    path('dersler/', include('dersler.urls')),
    path('users/', include('users.urls')),
    path('deprem/', include('deprem.urls')),
]
