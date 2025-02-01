from django.db import models
from django.urls import reverse

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('music/detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.artist + ' - ' + self.album_title


class Song(models.Model):
    song_title = models.CharField(max_length=10)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    is_fav = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.song_title

