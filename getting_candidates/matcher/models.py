from django.db import models
from recordings.models import *
# Create your models here.

class MatchReport(models.Model):
    songs = models.FileField()

class InputRecording(models.Model):
        artist = models.CharField(max_length=512)
        title = models.CharField(max_length=256, blank=True, null=True)
        isrc = models.CharField(max_length=30, blank=True, null=True)
        duration = models.CharField(max_length=256, blank=True, null=True)
        match = models.ForeignKey(Recording, on_delete=models.CASCADE, null=True, blank=True, related_name='matches')
        match_report = models.ForeignKey(MatchReport, on_delete=models.CASCADE, related_name='input_songs')
