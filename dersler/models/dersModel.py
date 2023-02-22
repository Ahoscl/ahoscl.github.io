import datetime

from django.db import models
from .kategoriModel import KategoriModel
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class DersModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Başlık')
    # resim = models.ImageField('')
    metin = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    yazar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanici')
    son_duzenleme = models.DateTimeField('Son Düzenlenme Tarihi', auto_now_add=datetime.datetime)
    kategori = models.ForeignKey(KategoriModel, on_delete=models.CASCADE, related_name='ders_kategori')

    def __str__(self):
        return f"{self.yazar} -- {self.title}"
