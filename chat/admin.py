from django.contrib import admin
from .models import Room, Message
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_uuid', 'user', 'room_name', 'created_at')
    search_fields = ('room_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_uuid', 'user', 'room', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)