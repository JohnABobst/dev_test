from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=256, unique=True)

class Recording(models.Model):
    artist = models.ForeignKey(Artist, related_name='artist_songs', on_delete=models.CASCADE, to_field='artist_name')
    title = models.CharField(max_length=256, blank=True, null=True)
    isrc = models.CharField(max_length=30, blank=True, null=True)
    duration = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        unique_together = ['artist', 'title', 'isrc', 'duration']
