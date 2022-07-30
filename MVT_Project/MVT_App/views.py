from django.shortcuts import render
from MVT_App.models import Familia

# Create your views here.

def familia(request):
    flia = Familia.objects.all()
    return render(request, "MVT_App/index.html", {"familia" : flia})
