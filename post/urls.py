from django.urls import path
from .views import AlbumListView, AlbumImageView, AlbumCreateView, AlbumDeleteView, AlbumUpdateView, AlbumDetailView

urlpatterns = [
    path('libro/<int:pk>/editar',AlbumUpdateView.as_view(), name = "libroEditar"),
    path('libro/<int:pk>/eliminar',AlbumDeleteView.as_view(), name = "libroEliminar"),
    path('libro/<int:pk>/nuevo',AlbumCreateView.as_view(), name = "libroNuevo"),
    path('libro/<int:pk>', AlbumDetailView.as_view(), name='libroDetalle'),
    path('libros/', AlbumImageView.as_view(), name='libros'),
    path('', AlbumListView.as_view(), name='home'),
]