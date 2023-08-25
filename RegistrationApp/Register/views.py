from django.shortcuts import render, redirect
from .forms import KullaniciKayitForm
from rest_framework import generics
from .models import Kullanici
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = Kullanici.objects.all()
    serializer_class = UserSerializer

def APİ(request):
    users = Kullanici.objects.all()
    return render(request, 'register/user_list.html', {'users': users})


def kayit_ol(request):
    if request.method == 'POST':
        form = KullaniciKayitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')
    else:
        form = KullaniciKayitForm()
    return render(request, 'register/register.html', {'form': form})

def kayit_basarili(request):
    return render(request, 'register/register_success.html')

