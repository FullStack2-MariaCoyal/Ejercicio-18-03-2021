from django.views.generic.list import ListView
from django.views.generic import DetailView, TemplateView
from .models import AlbumImage, Album

class AlbumListView(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'album'

class AlbumImageView(DetailView):
    model = AlbumImage
    template_name = "home.html"
    context_object_name = 'albumimage'