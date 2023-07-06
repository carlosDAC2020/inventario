from django.shortcuts import render, HttpResponse
# proteccion de rutas 
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"index.html")


def home(request):
    return render(request,"home.html")