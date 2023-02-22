from ..forms import KategoriForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def kategoriolustur(request):
    if request.method != 'POST':
        form = KategoriForm()
    else:
        form = KategoriForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('dersler:index')

    context = {'form': form}
    return render(request, 'kategoriOlustur.html', context)
