from django.db import models

# Create your models here.

class Genre(models.Model):
    sjanger = models.CharField(max_length=100)

    def __str__(self):
        return self.sjanger

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.song_name