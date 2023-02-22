from django.shortcuts import render, redirect


def index (request):
    context = {'bilgi': 'ANASAYFA DÜZENLENECEK'}
    return render(request, 'index.html', context)
