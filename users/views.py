from django.shortcuts import render,redirect
from .forms import UserCreationFormMe,UserChangeFormMe
from django.contrib.auth import login
from django.contrib.auth.models import User
# Create your views here.


# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationFormMe()
    else:
        form = UserCreationFormMe(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request,user_id):
    user=User.objects.get(id=user_id)
    deneme={'user':user}
    return render(request,'profile.html',deneme)


def editprofile(request):
    if request.method != 'POST':
        form = UserChangeFormMe()
    else:
        form = UserChangeFormMe(data=request.POST,instance=User)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)