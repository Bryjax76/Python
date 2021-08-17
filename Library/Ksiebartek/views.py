from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return HttpResponse("<strong>Witaj świecie!</strong>")

def papa(request):
    return HttpResponse("<strong>Żegnam ozięble!</strong>")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get("username"),
                                password=form.cleaned_data.get("password1"))
            login(request, user)
            return redirect("service-list")
        
    else:
        form = UserCreationForm()
    return render(request,
                  template_name="signup.html",
                  context={"form": form})
    
