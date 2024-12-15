import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blacklist.settings')
from app.models import Url
django.setup()



def llenadoLista(lista):
    object_url = Url.objects.create(
        url = "www.test.leo",
        cout = 0
    )
    print (f"Finish {object_url}")
    #for data in lista:
        
        #object_url = Url.objects.create(
        #    url = data
        #    cout = 0
        #)

        #ListaBlanca.objects.create(
        #    url=data
        #    clasificacion="usuario"
        #    tipoAmenaza="No definido"
        #)
        #print(f'url = {data}')
    #    print(data)

archivo = open("qrLists/respaldo/goodUrlList.txt", "r")
lista = archivo.readlines()
#print(lista)
llenadoLista(lista)