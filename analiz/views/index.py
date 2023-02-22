from django.shortcuts import redirect, render


def index (request):
    bilgi = 'DENEME SAYFASI'
    context = {'bilgi': bilgi}
    return render(request, 'aindex.html', context)
