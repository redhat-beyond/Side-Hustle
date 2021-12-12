from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def searchJob(request):
    return render(request, 'searchJob.html')


def home(request):
    return render(request, 'home.html')
