from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Il y a quelqu'un ici ?")

