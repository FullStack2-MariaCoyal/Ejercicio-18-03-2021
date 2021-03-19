from django.contrib import admin
from .models import Album, AlbumImage
# Register your models here.
admin.site.register(Album)
admin.site.register(AlbumImage)