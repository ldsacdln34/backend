from django.urls import path,include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'urls', views.UrlViewSet)
#router.register(r'check-url', views.UrlViewSet2)

urlpatterns = [
    path("", include(router.urls)),
    path("check-url", views.check_list)
]