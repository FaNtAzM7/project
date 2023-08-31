from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as rlog, logout
from .forms import RegUser
def login(request):
    redirect_url = reverse("profile")
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        rlog(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html')
def logout_view(request):
    logout(request)
    return redirect(reverse("login"))
def profile(request):
    return render(request,"app_auth/profile.html")
def register(request):
    if request.method == "POST":
        form = RegUser(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            rlog(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = RegUser()

    context = {'form': form}

    return render(request, 'app_auth/register.html', context)
