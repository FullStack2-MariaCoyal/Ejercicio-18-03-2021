from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AlbumImage, Album
from django.urls import reverse_lazy

class AlbumListView(ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'album'

class AlbumImageView(ListView):
    model = AlbumImage
    template_name = "libros.html"
    context_object_name = 'album2'

class AlbumDetailView(DetailView):
    model = AlbumImage
    template_name = "libroDetalle.html"
    context_object_name = 'lista'

class AlbumCreateView(CreateView): 
    model = AlbumImage
    template_name = 'libroNuevo.html'
    fields = '__all__'

class AlbumUpdateView(UpdateView):
    model = AlbumImage
    template_name = 'libroEditar.html'
    fields = '__all__'

class AlbumDeleteView(DeleteView):
    model = AlbumImage
    template_name = 'libroEliminar.html'
    context_object_name = 'lista'
    success_url = reverse_lazy('home')
