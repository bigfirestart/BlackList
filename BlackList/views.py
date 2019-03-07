from django.shortcuts import render
from .models import Item , Offender


def index(request):
    list = Item.objects.all()
    return render(request, 'index.html', {"list": list})
def offenders(request):
    list = Offender.objects.all()
    return render(request, 'offenders.html', {"list": list})
