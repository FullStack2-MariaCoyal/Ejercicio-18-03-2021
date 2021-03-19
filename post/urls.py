from django.urls import path
from .views import AlbumListView, AlbumImageView

urlpatterns = [
    path('libros/', AlbumImageView.as_view(), name='libros'),
    path('', AlbumListView.as_view(), name='home'),
    
]