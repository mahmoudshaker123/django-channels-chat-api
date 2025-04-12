from rest_framework.viewsets import ModelViewSet
from .models import Room, Message
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models import Count
from django.db import IntegrityError
from django.db.models import Q, Count
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from slugify import slugify


def chat_ui(request):
    return render(request, 'chat/index.html')


def get_users(request):
    users = User.objects.values('id', 'username')  
    return JsonResponse(list(users), safe=False)


def get_or_create_private_room(user1, user2):
    try:
        rooms = Room.objects.annotate(num_users=Count('user')).filter(
            users__in=[user1, user2]
        ).filter(num_users=2)

        if rooms.exists():
            return rooms.first()

        room_name = slugify(f'{user1.username}_{user2.username}')
        room = Room.objects.create(room_name=room_name)
        room.user.set([user1, user2])
        return room
    except IntegrityError:
        return None 


def create_room(name):
    room_name = slugify(name)   
    return Room.objects.create(room_name=room_name)


class ChatRoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [AllowAny]    

class ChatMessageViewSet(ModelViewSet):
    queryset = Message.objects.select_related('user', 'room').order_by('-created_at')
    serializer_class = ChatMessageSerializer 


    def get_queryset(self):
        room_uuid = self.request.query_params.get('room_uuid', None)   
        if room_uuid:
            return self.queryset.filter(room__room_uuid=room_uuid)
        return self.queryset


class UserListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = User.objects.values('id', 'username')
        return Response(users)