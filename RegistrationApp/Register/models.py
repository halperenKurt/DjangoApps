from django.db import models

class Kullanici(models.Model):
    kullanici_adi = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

