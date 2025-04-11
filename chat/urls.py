from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ChatRoomViewSet , ChatMessageViewSet , chat_ui
from . import views

router = DefaultRouter()
router.register('rooms', ChatRoomViewSet, basename='chatroom')  
router.register('messages', ChatMessageViewSet, basename='chatmessage')

urlpatterns = [
    path('api/' , include(router.urls) ),
    path('', chat_ui, name='chat_ui'),
    path('api/users/', views.get_users, name='get_users'),
    
]