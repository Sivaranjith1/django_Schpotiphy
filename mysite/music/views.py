from django.shortcuts import render
from .models import Album, Song

# Create your views here.

def home(request):
    return render(request, 'music/home.html')
