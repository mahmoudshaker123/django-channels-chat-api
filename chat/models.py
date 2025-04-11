from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    room_uuid= models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user= models.ManyToManyField(User)
    room_name = models.CharField(max_length=100 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room: {self.room_name}"

class Message(models.Model):
    message_uuid= models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    content = models.TextField()
    room = models.ForeignKey(Room ,on_delete=models.CASCADE ,related_name='messages') 
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + " in " + self.room.room_name + " : " + self.content[:20] + "..."
