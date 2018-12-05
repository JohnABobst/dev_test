from rest_framework import serializers
from recordings.models import *
from matcher.models import *
from recordings.serializers import *
import csv
from time import perf_counter
from functools import reduce
from django.db.models import Q
import sys
from django.forms.models import model_to_dict

class InputRecordingSerializer(serializers.ModelSerializer):
    match = RecordingSerializer()
    class Meta:
        model = InputRecording
        fields = '__all__'

class MatcherReportSeralizer(serializers.ModelSerializer):
    match_choices = serializers.SerializerMethodField()
    input_songs = InputRecordingSerializer(many=True, read_only=True)

    class Meta:
        model = MatchReport
        fields = '__all__'

    def create(self, validated_data):
        #Overriding create method to assign Input songs to Match Records
        instance = super().create(validated_data)
        instance.save()
        with open(str(instance.songs), newline='') as csvfile:
            songs = csv.DictReader(csvfile)
            for row in songs:
                dict = {key:value for (key,value) in row.items()}
                dict['match_report'] = instance
                InputRecording.objects.create(**dict)
        return instance

    #function that must be defined when a seralizer field is used.
    def get_match_choices(self, obj):
        #A list to store input songs and their possible matches
        match_choices = []
        #Captures the CSV file from the request

        with open(str(obj.songs), newline='') as csvfile:
            songs = csv.DictReader(csvfile)
            for row in songs:

                '''
                Searching by artist first to cut down on data that needs to be searched when filter is applieds.
                This should cut down search time in a larger database
                '''
                song = {key:value for (key,value) in row.items()}
                dict = {key:value for (key,value) in row.items()}

                #Creates a dictionary of values to unpack, excluding empty strings, for built in Django filter function,
                junk_song = {key:value.split(" ") for (key,value) in row.items() if value != ''}
                artist = junk_song.pop('artist')

                kwargs_list = []
                for key, values in junk_song.items():
                    for value in values:
                        kwargs_list.append({key+'__contains':value})
                #Try block in case no artist is found in the event of a typo.  If no artist is returned, except block will filter by other fields only.
                try:

                    #returns any song by that artist, even if artist name has other artists included.
                    matching_artists = reduce(lambda x,y: x| y, map(lambda arg: Artist.objects.filter(artist_name__contains=arg), artist))
                    #returns search queries for all artists in the list
                    artist_song_queries = [x.artist_songs.all() for x in matching_artists]

                    #Reduce list of search queries in the case that multiple artists were found.
                    #Returns a searchquery object so that filter() method of searchquery can still be used.
                    matching_songs = reduce(lambda x,y: x|y, artist_song_queries)

                    #filters songs by isrc kwarg
                    try:
                        isrc_kwarg = [x for x in kwargs_list if 'isrc__contains' in x]
                        #removes kwarg so that it won't be repeated if no results are returned and other filters are applied
                        kwargs_list.remove(isrc_kwarg[0])
                        matching_songs = artist_song_query.filter(isrc_kwarg[0])
                    except:
                        matching_songs = reduce(lambda x,y: x| y, map(lambda kwarg: Recording.objects.filter(**kwarg), kwargs_list))


                except:
                    #Another try for isrc kwarg in the event that artist query failed
                    try:
                        isrc_kwarg = [x for x in kwargs_list if 'isrc__contains' in x]
                        #removes kwarg so that it won't be repeated if no results are returned and other filters are applied
                        kwargs_list.remove(isrc_kwarg[0])
                        matching_songs = Recording.objects.filter(**isrc_kwarg[0])
                    #If isrc query and artist query fails, it will bring back all songs that match the remaining criteria
                    except:
                        matching_songs = reduce(lambda x,y: x| y, map(lambda kwarg: matching_songs.filter(**kwarg), kwargs_list))


                possible_matches = []
                for song_match in matching_songs:
                    weight = {'isrc': 4, 'artist': 3, 'title': 3, 'duration': 1}
                    match = model_to_dict(song_match, fields=[field.name for field in song_match._meta.fields])
                    id = match.pop('id')
                    weight_divider = sum([value for (key,value) in weight.items() if song[key] != "" or song[key] != "Field Missing"])
                    weight_of_song = int(sum([value for (key,value) in weight.items() if song[key] == match[key] and song[key] != "Field Missing"]) *100)
                    match['match_percentage'] = int( weight_of_song/weight_divider)
                    match['id'] = id
                    if match['match_percentage'] > 40:
                        possible_matches.append(match)
                if possible_matches == []:
                    possible_matches.append({'match_percentage': 'There are no matches in the database'})

                #Attempts to get input recording that matches song so that it's id can be used on the front end
                try:
                    input_recording = obj.input_songs.all().get(**song)
                    song['id'] = input_recording.id
                except:
                    #Creates an input recording if none exists
                    InputRecording.objects.create(match_report=obj, **song)
                #Sorts list of dictinoaries by match percentage key
                sorted_possible_matches = sorted(possible_matches, key= lambda key: key['match_percentage'], reverse=True)

                #Appends song and pssible matches to match choices
                match_choices.append({'song': song, 'possible_matches': sorted_possible_matches})
            return(match_choices)
