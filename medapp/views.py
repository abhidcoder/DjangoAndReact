#from django.urls import HttpResponse
from django.http import HttpResponse,JsonResponse

def fetch_data(request):

    return HttpResponse("Welcome to Django")

def ping(request):
    print("ping Djnago")
    return HttpResponse("<h1> Ping Django </h1>")