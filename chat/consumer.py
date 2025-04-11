from .models import Message , Room
from .serializers import ChatMessageSerializer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from slugify import slugify

from channels.db import database_sync_to_async


@database_sync_to_async
def save_message(username, room_name, message):
    user = User.objects.get(username=username)
    room = Room.objects.get(room_name=room_name)
    return Message.objects.create(user=user, room=room, content=message)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group = f'chat_{slugify(self.room_name)}'  # تحويل اسم الغرفة إلى صيغة مقبولة

        # Join room group
        await self.channel_layer.group_add(
            self.room_group,
            self.channel_name
        )

        await self.accept()


    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group,
            self.channel_name
        )


    
    async def receive(self, text_data ):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await save_message(username, self.room_name, message)

        await self.channel_layer.group_send(
            self.room_group,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )


    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'message': message,
                'username': username
            }))

