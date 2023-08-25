from rest_framework import serializers
from .models import Kullanici

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = '__all__'