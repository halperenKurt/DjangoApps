from django import forms
from .models import Kullanici

class KullaniciKayitForm(forms.ModelForm):
    class Meta:
        model = Kullanici
        fields = ['kullanici_adi', 'email']
