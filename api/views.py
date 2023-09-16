from django.shortcuts import render
from rest_framework import viewsets
from api.models import Api
from api.serializers import ApiSerializer

# Create your views here.
class RestApi(viewsets.ModelViewSet):
    queryset=Api.objects.all()
    serializer_class=ApiSerializer
