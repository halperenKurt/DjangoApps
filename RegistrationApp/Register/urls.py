from django.urls import path
from . import views
from .views import UserList


urlpatterns = [
    path('register/', views.kayit_ol, name='register'),
    path('register_success/', views.kayit_basarili, name='register_success'),
    path('users/', views.APİ, name='user-list'),
]
