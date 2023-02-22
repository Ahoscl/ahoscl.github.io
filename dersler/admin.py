from django.contrib import admin
from .models.dersModel import DersModel
from .models.kategoriModel import KategoriModel

# Register your models here.

admin.site.register(DersModel)
admin.site.register(KategoriModel)