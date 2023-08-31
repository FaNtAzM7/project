from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Advert
from .forms import AdvertForm

def index(request):
    advert=Advert.objects.all()
    context={"advert":advert}
    return render(request,"app_adv/index.html",context)
def top_sellers(request):
    return render(request,"app_adv/top_sellers.html")
def advertisement(request):
    return render(request,"app_adv/advertisement.html")
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
    return render(request,"app_adv/advertisement_post.html",context)


