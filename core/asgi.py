
import os
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from chat.consumer import ChatConsumer
from django.urls import path

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
            
        ])
    ),
})
