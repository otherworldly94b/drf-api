from django.urls import path

from . import views

app_name = 'messaging'

urlpatterns = [
  path('send-message/', views.SendMessageView.as_view(), name='send-message'),
  path('inbox/', views.InboxView.as_view(), name='inbox'),
]
