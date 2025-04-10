from rest_framework import serializers
from .models import Room , Message


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_uuid', 'user', 'room_name', 'created_at']


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_uuid', 'content', 'room', 'user', 'created_at']