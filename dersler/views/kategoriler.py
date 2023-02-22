from ..models import KategoriModel,DersModel
from django.shortcuts import render
from django.db.models import Count


def kategoriler(request):

    kategoriler=KategoriModel.objects.annotate(total=Count('ders_kategori')).all()

    context ={'kategoriler':kategoriler,}

    return render(request, 'kategoriler.html',context)