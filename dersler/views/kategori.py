from ..models import KategoriModel
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def kategori (request, topic_id):
    kategori = KategoriModel.objects.get(id = topic_id)
    dersler = kategori.entry_set.order_by('-date_added')
    context = {'kategori': kategori, 'dersler': dersler}
    return render(request, 'dindex.html', context)