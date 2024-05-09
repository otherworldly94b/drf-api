from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Message
from .serializers import MessageSerializer

class SendMessageView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request, format=None):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
      sender = request.user
      recipient_username = request.data["recipient_username"]
      content = request.data["content"]

      # Check if recipient exists
      try:
        recipient = User.objects.get(username=recipient_username)
      except User.DoesNotExist:
        return Response({"error": "Recipient user not found"}, status=400)

      message = Message.objects.create(sender=sender, recipient=recipient, content=content)
      serializer = MessageSerializer(message)
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class InboxView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, format=None):
    user = request.user
    messages = Message.objects.filter(recipient=user).order_by("-timestamp")
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
