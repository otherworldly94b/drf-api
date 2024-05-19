from rest_framework import status
from rest_framework import generics, permissions,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import User


class SendMessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()  
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        recipient_username = self.request.data.get("recipient_username")

        if not recipient_username:
            raise serializers.ValidationError({"recipient_username": "This field is required."})

        try:
            recipient = User.objects.get(username=recipient_username)
            serializer.save(sender=self.request.user, recipient=recipient)
        except User.DoesNotExist:
            raise serializers.ValidationError({"recipient_username": "Recipient not found."})


class InboxView(APIView):
    """
    View for retrieving messages received by the authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Retrieves all messages received by the authenticated user.
        """
        user = request.user
        messages = Message.objects.filter(recipient=user).order_by("-timestamp")
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class SingleMessageView(generics.RetrieveAPIView):
    """
    Retrieve a single received message by its ID. Requires authentication.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filters messages to only include those received by the authenticated user.
        """
        user = self.request.user
        return Message.objects.filter(recipient=user)

    def get_object(self):
        """
        Retrieves the message object with the requested ID, ensuring it's a received message.
        """
        queryset = self.get_queryset()
        pk = self.kwargs['pk']
        try:
            return queryset.get(pk=pk)
        except Message.DoesNotExist:
            return None
