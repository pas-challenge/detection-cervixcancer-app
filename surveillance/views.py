from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Overview(request):
    return render(request, 'overview.html')


def Departement(request):
    return render(request, 'department.html')


def Doctor(request):
    return render(request, 'doctor.html')


def Survey(request):
    zones = Zone.objects.all()
    dossiers = Dossier.objects.all()
    print(dossiers[0])
    return render(request, 'appoinment.html', {'zones': zones, 'dossiers': dossiers})


def Patiente(request, numero):
    dossier = Dossier.objects.get(numero=numero)
    print(dossier)
    return render(request, 'patiente.html', {'dossier': dossier})


def Validation(request, id):
    diagnostic = Diagnostic.objects.get(id=id)
    print(diagnostic.prediction)
    if diagnostic.prediction == 0:
        label = "Négatif"
    label = "Positif"
    return render(request, 'validation.html', {'diagnostic': diagnostic, 'label': label})
