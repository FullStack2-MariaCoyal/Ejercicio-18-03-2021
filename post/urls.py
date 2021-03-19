from django.urls import path
from .views import AlbumListView, AlbumImageView

urlpatterns = [
    path('', AlbumListView.as_view(), name='home'),
    path('image/<int:pk>', AlbumImageView.as_view(), name='home'),
    
]