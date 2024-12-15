from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializer import UrlSerializer, UrlSerializer2
from .models import Url, BlackList

from rest_framework.decorators import api_view
from rest_framework.response import Response

class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


#class UrlViewSet2(viewsets.ModelViewSet):
#    queryset = BlackList.objects.all()
#    serializer_class = UrlSerializer2

@api_view(['GET', 'POST'])
def check_list(request):
    is_white_list = "aceptado"
    result = checkBlackList(request.data.url)

    return Response({
        'status_scan': is_white_list, 
        'url': "www.leo.com",
    })


def checkBlackList(url):

    return True