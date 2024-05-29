# from rest_framework import serializers
# from profiles.serializers import ProfileSerializer
# from .models import Message

# class MessageSerializer(serializers.ModelSerializer):
#     recipient_profile = ProfileSerializer(read_only=True)
#     sender_profile = ProfileSerializer(read_only=True)

#     class Meta:
#         model = Message
#         fields = ['id', 'owner', 'sender', 'recipient', 'recipient_profile', 'sender_profile' ,'content', 'is_read', 'timestamp']
    
#     def __init__(self, *args, **kwargs):
#         super(MessageSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         if request and request.method=='POST':
#             self.Meta.depth = 0
#         else:
#             self.Meta.depth = 2