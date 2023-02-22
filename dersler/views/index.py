from django.shortcuts import render, redirect
from ..models import DersModel
from ..models import KategoriModel


def index(request):
    dersler = DersModel.objects.all()
    kategori = KategoriModel.objects.all()

    context = {
        'dersler': dersler,
        'kategori': kategori,
    }
    return render(request, 'dindex.html', context)
