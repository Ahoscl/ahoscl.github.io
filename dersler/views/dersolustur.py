from ..forms import DersForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def dersolustur(request):
    if request.method != 'POST':
        form = DersForm()
    else:
        form = DersForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dersler:index')

    context = {'form': form}
    return render(request, 'dersolustur.html', context)
