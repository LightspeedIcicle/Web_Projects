from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render("request, website/index.html")


def rates(request):
    return render("request, website/rates.html")


def summitGrill(request):
    return render("request, website/summitGrill.html")


def info(request):
    return render("request, website/info.html")
