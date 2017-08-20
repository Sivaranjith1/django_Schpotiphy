from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic

from .models import Genre, Album, Song


# Create your views here.

def home(request):
    return render(request, 'music/home.html')

class GenreList(generic.ListView):
    template_name = 'music/genre.html'
    context_object_name = 'genre'

    def get_queryset(self):
        return Genre.objects.order_by('sjanger')

def genreView(request, sjanger_id):
    sjanger = get_object_or_404(Genre, pk=sjanger_id)
    sang = get_list_or_404(Song)
    return render(request, 'music/genreList.html', {'sjanger':sjanger, 'sang': sang})

def play(request, sang_id):
    sang = get_object_or_404(Song, pk=sang_id)
    return render(request, 'music/song.html', {'sang':sang})