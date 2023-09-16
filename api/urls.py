from django.contrib import admin
from django.urls import path,include
from api.views import RestApi
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'crud',RestApi)

urlpatterns = [
    path("",include(router.urls))
]
