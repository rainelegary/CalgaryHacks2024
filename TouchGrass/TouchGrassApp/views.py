from django.shortcuts import render
from .models import Facility


def index(request):
    return render(request, 'TouchGrassApp/index.html')

def map_view(request):
    facilities = Facility.objects.all()  # Query all facilities from your database
    context = {
        'facilities': facilities
    }
    return render(request, 'TouchGrassApp/index.html', context)