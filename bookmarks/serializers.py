from django.db import IntegrityError
from rest_framework import serializers
from bookmarks.models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
  """
  Serializer for the Bookmark model
  The create method handles the unique constraint on 'owner' and 'post'
  """
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = Bookmark
    fields = ['id', 'owner', 'bookmarked_post']

  def create(self, validated_data):
    try:
      return super().create(validated_data)
    except IntegrityError:
      raise serializers.ValidationError({
          'detail': 'You already bookmarked this post.'
      })
