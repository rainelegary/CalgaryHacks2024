from django.shortcuts import render
from .models import Facility


def index(request):
    facilities = Facility.objects.all()
    print( {'facilities': facilities})
    return render(request, 'TouchGrassApp/index.html', {'facilities': facilities})