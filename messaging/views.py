# from rest_framework import generics, permissions,serializers
# from django.db.models import OuterRef, Subquery
# from django.db.models import Q
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated
# from .models import Message
# from .serializers import MessageSerializer
# from django.contrib.auth.models import User

# # owner_id
# class InboxView(generics.ListAPIView):
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         user = self.request.user
#         messages = Message.objects.filter(recipient=user).annotate(
#             sender_username=serializers.CharField(source='sender.username')
#         )
#         return messages
#         # serialized_data = self.get_serializer(messages, many=True)
#         # for message in serialized_data.data:
#         #     print(message['sender_username'])  # Access annotated field
#         #     return messages


#     # """
#     # View for retrieving messages received by the user.
#     # """
#     # serializer_class = MessageSerializer
#     # permission_classes = [IsAuthenticated]

#     # def get_queryset(self):
#     #     owner_id = self.kwargs['owner_id']

#     #     messages = Message.objects.filter(
#     #         id__in =  Subquery(
#     #             Owner.objects.filter(
#     #                 Q(sender__recipient=owner_id) |
#     #                 Q(recipient__sender=owner_id)
#     #             ).distinct().annotate(
#     #                 last_msg=Subquery(
#     #                     Message.objects.filter(
#     #                         Q(sender=OuterRef('id'),recipient=owner_id) |
#     #                         Q(recipient=OuterRef('id'),sender=owner_id)
#     #                     ).order_by('-id')[:1].values_list('id', flat=True) 
#     #                 )
#     #             ).values_list('last_msg', flat=True).order_by("-id")
#     #         )
#     #     ).order_by("-id")
            
#     #     return messages

# class GetMessages(generics.ListAPIView):
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         sender_id = self.kwargs['sender_id']
#         recipient_id = self.kwargs['recipient_id']
#         messages =  Message.objects.filter(
#             sender__in=[sender_id, recipient_id], 
#             recipient__in=[sender_id, recipient_id])
#         return messages
    
# class SendMessages(generics.CreateAPIView):
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated]


# # class SendMessageView(generics.ListCreateAPIView):
# #     queryset = Message.objects.all()  
# #     serializer_class = MessageSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# #     def perform_create(self, serializer):
# #         recipient_username = self.request.data.get("recipient_username")

# #         if not recipient_username:
# #             raise serializers.ValidationError({"recipient_username": "This field is required."})

# #         try:
# #             recipient = User.objects.get(username=recipient_username)
# #             serializer.save(sender=self.request.user, recipient=recipient)
# #         except User.DoesNotExist:
# #             raise serializers.ValidationError({"recipient_username": "Recipient not found."})


# # class InboxView(generics.ListCreateAPIView):
# #     """
# #     View for retrieving messages received by the authenticated user.
# #     """
    
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request, format=None):
# #         """
# #         Retrieves all messages received by the authenticated user.
# #         """
# #         user = request.user
# #         messages = Message.objects.filter(recipient=user).order_by("-timestamp")
# #         serializer = MessageSerializer(messages, many=True)
# #         return Response(serializer.data)




# # class InboxView(generics.ListAPIView): owner_id
# #     """
# #     View for retrieving messages received by the user.
# #     """
# #     serializer_class = MessageSerializer

# #     def get_queryset(self):
# #         owner_id = self.kwargs['owner_id']

# #         messages = Message.objects.filter(
# #             id__in =  Subquery(
# #                 Owner.objects.filter(
# #                     Q(sender__recipient=owner_id) |
# #                     Q(recipient__sender=owner_id)
# #                 ).distinct().annotate(
# #                     last_msg=Subquery(
# #                         Message.objects.filter(
# #                             Q(sender=OuterRef('id'),recipient=owner_id) |
# #                             Q(recipient=OuterRef('id'),sender=owner_id)
# #                         ).order_by('-id')[:1].values_list('id', flat=True) 
# #                     )
# #                 ).values_list('last_msg', flat=True).order_by("-id")
# #             )
# #         ).order_by("-id")
            
# #         return messages

# # class SingleMessageView(generics.RetrieveAPIView):
# #     """
# #     Retrieve a single received message by its ID. Requires authentication.
# #     """
# #     serializer_class = MessageSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# #     def get_queryset(self):
# #         """
# #         Filters messages to only include those received by the authenticated user.
# #         """
# #         user = self.request.user
# #         return Message.objects.filter(recipient=user)

# #     def get_object(self):
# #         """
# #         Retrieves the message object with the requested ID, ensuring it's a received message.
# #         """
# #         queryset = self.get_queryset()
# #         pk = self.kwargs['pk']
# #         try:
# #             return queryset.get(pk=pk)
# #         except Message.DoesNotExist:
# #             return None


