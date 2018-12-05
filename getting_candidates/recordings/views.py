from django.shortcuts import render
from recordings.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from recordings.models import Recording
from rest_framework.decorators import api_view
import csv
# Create your views here.
class RecordingView(generics.ListCreateAPIView):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

#View to upload songs to database.  Not connected to a model
@api_view(['GET', 'POST'])
def upload_view(request):
    if request.method == 'POST':
        with open(str(request.FILES['songs']), newline='') as csvfile:
            recordings = csv.DictReader(csvfile)
            for row in recordings:
                #Creates a dictionary from the list of tuples
                dict = {key:value for (key, value) in row.items()}
                artist = dict.pop('artist')
                try:
                    song_artist = Artist.objects.create(artist_name=artist)
                    song_artist.save()
                    dict['artist'] = song_artist
                except:
                    song_artist = Artist.objects.get(artist_name=artist)
                    dict['artist'] = song_artist
                try:
                    recording = Recording.objects.get(**dict)

                except:
                    Recording.objects.create(**dict)

                recordings = Recording.objects.all()
            return Response((RecordingSerializer(recordings, many=True).data))

@api_view(['GET', 'POST'])
def add_song(request):
    if request.method == 'POST':
        artist_name = request.data.pop('artist')
        try:
            artist = Artist.objects.create(artist_name=artist_name)

        except:
            artist = Artist.objects.get(artist_name=artist_name)
            
        try:
            song = Recording.objects.create(**request.data, artist=artist)
            song.save()
        except:
            song = Recording.objects.get(**request.data, artist=artist)
    return Response(RecordingSerializer(song).data)
