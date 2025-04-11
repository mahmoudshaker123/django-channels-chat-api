from django.contrib import admin
from .models import Room, Message
# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_uuid', 'display_users', 'room_name', 'created_at')
    search_fields = ('room_name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def display_users(self, obj):
        return ", ".join([user.username for user in obj.user.all()])
    display_users.short_description = 'Users'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_uuid', 'user', 'room', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)