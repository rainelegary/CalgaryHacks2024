from django.shortcuts import render
from .models import Facility


def homescreen(request):
    return render(request, 'TouchGrassApp/base.html')

def index(request):
    return render(request, 'TouchGrassApp/index.html')

def map_view(request):
    facilities = Facility.objects.all()  # Query all facilities from your database
    context = {
        'facilities': facilities
    }
    return render(request, 'TouchGrassApp/index.html', context)

def index(request):
    facilities = Facility.objects.all()
    print( {'facilities': facilities})
    return render(request, 'TouchGrassApp/index.html', {'facilities': facilities})