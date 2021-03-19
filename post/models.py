from django.db import models

class Album(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    saga = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.saga

class AlbumImage(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to='static/img/')
    def __str__(self):
        return self.name

