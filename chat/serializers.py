from rest_framework import serializers
from .models import Room , Message


class ChatRoomSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['room_uuid', 'users', 'room_name', 'created_at']

    def get_users(self, obj):
        return [user.username for user in obj.user.all()]  



    
    
class ChatMessageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['message_uuid', 'content', 'room', 'user', 'created_at']

    def get_user(self, obj: Message):
        return obj.user.username if obj.user else None

    def get_room(self, obj: Message):
        return obj.room.room_name if obj.room else None
