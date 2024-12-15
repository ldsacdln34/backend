from django.shortcuts import render
from .serializer import UrlSerializer, UrlSerializer2
from .models import Url, BlackList,WhiteList, Graylist
import requests 
import json
import time

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


#class UrlViewSet2(viewsets.ModelViewSet):
#    queryset = BlackList.objects.all()
#    serializer_class = UrlSerializer2

@api_view(['POST'])
def check_list(request):
    #url = "https://www.facebuook.com"

    url = request.data.get("url")
    result = checkList(url)

    return Response({
        'status_scan': result, 
        'url': url,
    })

@api_view(['POST'])
def sandbox(request):
    try:
        url = request.data.get("url")
        page_data = requests.get(url)
        status_code = page_data.status_code
        content = page_data.text
        status_scan = "whiteList" 
        time.sleep(5)
    except:
        status_code = "indeterminado"
        content = ""
        status_scan = 404 



    return Response({  
        'status_scan': status_scan,
        'url': url,
        'status_code': status_code,
        'web_page': content
    })


def checkList(url):

    mydata = BlackList.objects.filter(url__url=url).first()
    if not mydata:         
         mydata = WhiteList.objects.filter(url__url=url).first()
         if not mydata:
             mydata =Graylist.objects.filter(url__url=url).first()
             if not mydata:
                 result= apiTerceros(url)
                 return result
             else:
                 return "grayList"
         else:
          return "whiteList"
    else:
        return "blackList"
    
    return "indeterminado"

def apiTerceros(url):
    url_tercero = "https://www.virustotal.com/api/v3/urls"
    Key = "7fa6a9b0a5e3f48e078845224e9d3ddcb52fd5e02d8b57a24af500cf63d1010b"

    
    payload = { "url":url }
    headers = {
        "accept": "application/json",
        "x-apikey": Key,
        "content-type": "application/x-www-form-urlencoded"

     }
    try:
        report_response = requests.post(url_tercero, data=payload, headers=headers)
        report_id = report_response.json()["data"]["id"]
        api_url = f"https://www.virustotal.com/api/v3/analyses/{report_id}"
        headers = {
            "accept": "application/json",
            "x-apikey": Key
         }
        response_consult = requests.get(api_url, headers=headers)
        try: 
            stats = response_consult.json()["data"]["attributes"]["stats"]["malicious"]
            if stats > 0:
                return "blackList"
            else:
                return "indeterminado"
        except:
            print("sucedio un error con la segunda consulta")
    except:
        print("Sucedio un error con la primera consulta")
    return "indeterminado"






        