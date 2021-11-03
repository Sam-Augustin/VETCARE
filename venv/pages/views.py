from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def Diseases(request):
    return render(request, 'pages/Diseases.html')

def Fdisease(request):
    return render(request, 'pages/Fdisease.html')

def healthylife(request):
    return render(request, 'pages/healthylife.html')

def Appoint(request):
    return render(request, 'pages/Appoint.html')

def Contacts(request):
    return render(request, 'pages/Contacts.html')
