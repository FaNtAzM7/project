from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Advert
from .forms import AdvertForm

def index(request):
    advert=Advert.objects.all()
    context={"advert":advert}
    return render(request,"index.html",context)
def top_sellers(request):
    return render(request,"top_sellers.html")
def advertisement(request):
    return render(request,"advertisement.html")
def advertisement_post(request):
    if request.method=="POST":
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            advert=Advert(**form.cleaned_data)
            advert.user=request.user
            advert.save()
            url=reverse("index")
            return redirect(url)
    else:
        form = AdvertForm()
    context={"form":form}
    return render(request,"advertisement_post.html",context)
def login(request):
    return render(request,"login.html")
def profile(request):
    return render(request,"profile.html")
def register(request):
    return render(request,"register.html")

