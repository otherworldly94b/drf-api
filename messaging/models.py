from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
  recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.sender.username} to {self.recipient.username}: {self.content[:20]}"
