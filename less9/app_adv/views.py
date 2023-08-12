from django.shortcuts import render
from django.http import HttpResponse
from .models import Advert

def index(request):
    advert=Advert.objects.all()
    context={"advert":advert}
    return render(request,"index.html",context)
def top_sellers(request):
    return render(request,"top_sellers.html")
def advertisement(request):
    return render(request,"advertisement.html")
def advertisement_post(request):
    return render(request,"advertisement_post.html")
def login(request):
    return render(request,"login.html")
def profile(request):
    return render(request,"profile.html")
def register(request):
    return render(request,"register.html")

