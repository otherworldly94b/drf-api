from django.urls import path
# from .views import send_message, InboxView, SingleMessageView
from .views import SendMessageView, InboxView, SingleMessageView

urlpatterns = [
    # path('send-message/', send_message, name='send-message'),  # Function reference
    path('send-message/', SendMessageView.as_view(), name='send-message'),  # Function reference
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('messages/<int:pk>/', SingleMessageView.as_view(), name='single-message'),
]
