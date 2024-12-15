from django.shortcuts import render


from rest_framework import viewsets
from .serializer import UrlSerializer, UrlSerializer2
from .models import Url, BlackList,WhiteList, Graylist
import requests 

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
    url = "https://www.facebuook.com"
    result = checkList(url)
    print(result)


    return Response({
        'status_scan': result, 
        'url': "www.leo.com",
    })


def checkList(url):

    mydata = BlackList.objects.filter(url__url=url).first()
    if not mydata:         
         mydata = WhiteList.objects.filter(url__url=url).first()
         if not mydata:
             mydata =Graylist.objects.filter(url__url=url).first()
             if not mydata:
                 result= apiTerceros(url)
                 print (result)
                 return result
             else:
                 return "Gray List"
         else:
          return "White List"
    else:
        return "Black List"
    
    return ""

def apiTerceros(url):
    Key = "6c17899cc957d571c00ab9b01e4179fde72c9bf5980b94d26cc158c1f8be1a73"
    payload = { "url":url }

    headers = {
        "accept": "application/json",
        "x-apikey": Key,
        "content-type": "application/x-www-form-urlencoded"

     }
    report_response = requests.post(url, data=payload, headers=headers)
    report_id = report_response.json()["data"]["id"]
    api_url = f"https://www.virustotal.com/api/v3/analyses/{report_id}"
    headers = {
        "accept": "application/json",
        "x-apikey": "6c17899cc957d571c00ab9b01e4179fde72c9bf5980b94d26cc158c1f8be1a73"
     }
    response_consult = requests.get(api_url, headers=headers)
    stats = response_consult.json()["data"]["attributes"]["stats"]["malicius"]
    if stats > 0:
        return "Black List"
    else:
        return "Indeterminado Virus total"
    return ""






        