from ..models import KategoriModel,DersModel
from django.shortcuts import render
from django.db.models import Count


def ders_ayrinti(request, ders_id):

    ders=DersModel.objects.get(id=ders_id)
    print(ders)

    context ={'ders':ders}

    return render(request, 'dersayrinti.html',context)