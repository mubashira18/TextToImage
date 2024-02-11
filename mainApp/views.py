from django.http import HttpResponse
from django.shortcuts import render
from mainApp.models import TTI


def mainPage(request):
    return render(request, 'mainTemp/home.html', {})
