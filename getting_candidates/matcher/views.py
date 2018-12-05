from django.shortcuts import render
from rest_framework import generics
from matcher.serializers import *
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

# Create your views here.
class MatcherReportView(generics.ListCreateAPIView):
    queryset = MatchReport.objects.all()
    serializer_class = MatcherReportSeralizer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

#Function based view to handle creating relationship between input songs and songs in the database
@api_view(['GET', 'POST'])
def select_match(request, match_id, input_recording_id):
    if request.method == 'POST':
        match = Recording.objects.get(id=match_id)
        input_recording = InputRecording.objects.get(id=input_recording_id)
        match.matches.add(input_recording) 

        return(Response("Song selected successfully"))
