# from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from .forms import RegisterForm


def home_page(request):
    return render(request, "home.html", {"title": "Yahallo Minna"})


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    cform = ContactForm(data=request.POST or None)
    if cform.is_valid():
        print(cform.cleaned_data)
    return render(request, "contact.html", {"title": "Contact Us"})


def register_page(request):
    rform = RegisterForm(data=request.POST or None)
    print(request.POST)
    print(rform)
    if rform.is_valid():
        print(rform.cleaned_data)
    return render(request, "register.html", {"title": "Registration Form"})


def login_page(request):
    return render(request, "login.html", {"title": "Login"})


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)