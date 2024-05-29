# from django.contrib.auth import get_user_model
# from django.db import models
# from profiles.models import Profile


# User = get_user_model()

# class Message(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
#     sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")
#     recipient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reciever")

#     content = models.TextField(max_length=10000000000)

#     is_read = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['timestamp']
#         verbose_name_plural = "Message"

#     def __str__(self):
#         return f"{self.sender} - {self.recipient}"

#     @property
#     def sender_profile(self):
#         sender_profile = Profile.objects.get(owner=self.sender)
#         return sender_profile
#     @property
#     def recipient_profile(self):
#         recipient_profile = Profile.objects.get(owner=self.recipient)
#         return recipient_profile