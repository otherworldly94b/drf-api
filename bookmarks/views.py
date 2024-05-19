from rest_framework import generics, permissions
from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer

class BookmarkList(generics.ListCreateAPIView):
  """
  List bookmarks or create a bookmark if logged in.
  """
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  serializer_class = BookmarkSerializer
  queryset = Bookmark.objects.all()

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class BookmarkDetail(generics.RetrieveDestroyAPIView):
  """
  Retrieve a bookmark or delete it by id if you own it.
  """
  permission_classes = [permissions.IsOwnerOrReadOnly]
  serializer_class = BookmarkSerializer
  queryset = Bookmark.objects.all()
