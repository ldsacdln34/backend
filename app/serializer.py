from rest_framework import serializers
from .models import Url, BlackList

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model=Url
        #fields=("url","cout")
        fields="__all__"

class UrlSerializer2(serializers.ModelSerializer):
    class Meta:
        model=BlackList
        #fields=("url","cout")
        fields="__all__"
