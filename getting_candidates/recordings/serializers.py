from rest_framework import serializers
from recordings.models import *

class RecordingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recording
        fields = '__all__'
