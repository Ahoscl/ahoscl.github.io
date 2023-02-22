from django.db import models

# Create your models here.


class Deprem(models.Model):
    olus_zamani=models.DateTimeField(verbose_name = 'Tarih-Saat')
    enlem=models.CharField(max_length = 7,verbose_name = 'Enlem')
    boylam=models.CharField(max_length = 7,verbose_name = 'Boylam')
    derinlik=models.FloatField(verbose_name = 'Derinlik (km)')
    buyukluk=models.FloatField(verbose_name = 'Büyüklük')
    yer=models.CharField(max_length = 200,verbose_name = 'Yer')
    def __str__(self):
        return f"{self.olus_zamani},{self.enlem},self.boylam,self.derinlik,self.buyukluk,{self.yer}"
