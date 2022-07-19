from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
       # fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
        
