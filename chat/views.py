from rest_framework.viewsets import ModelViewSet
from .models import Room, Message
from .serializers import ChatRoomSerializer, ChatMessageSerializer
# Create your views here.

class ChatRoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = ChatRoomSerializer

class ChatMessageViewSet(ModelViewSet):
    queryset = Message.objects.select_related('user', 'room').order_by('-created_at')
    serializer_class = ChatMessageSerializer 


    def get_queryset(self):
        room_uuid = self.request.query_params.get('room_id' , None)
        if room_uuid:
                return self.queryset.filter(room__room_uuid=room_uuid)
        return self.queryset