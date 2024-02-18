# TouchGrass/TouchGrassApp/urls.py

from django.urls import path
from . import views
#from .views import homescreen


urlpatterns = [
    path('pagetwo', views.index, name='index'),
    path('', views.homescreen, name='homescreen'),
    #path('homescreen/', homescreen, name='homescreen'),

]