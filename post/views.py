from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import AlbumImage, Album

class AlbumListView(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'album'

class AlbumImageView(ListView):
    model = AlbumImage
    template_name = "libros.html"
    context_object_name = 'album2'