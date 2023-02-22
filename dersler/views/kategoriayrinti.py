from ..models import KategoriModel,DersModel
from django.shortcuts import render
from django.db.models import Count


def kategori_ayrinti(request, kategori_id):

    kategori_ayrinti=KategoriModel.objects.annotate(total=Count('ders_kategori')).get(id=kategori_id)
    ders=DersModel.objects.filter(kategori_id=kategori_id)
    context ={'kategori_ayrinti':kategori_ayrinti,
              'ders':ders}

    return render(request, 'kategoriayrinti.html',context)