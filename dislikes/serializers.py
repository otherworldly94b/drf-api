from django.db import IntegrityError
from rest_framework import serializers
from dislikes.models import Dislike


class DislikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Dislike model
    The create method handles the unique constraint on 'owner' and 'dislike_post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Dislike
        fields = ['id', 'created_at', 'owner', 'dislike_post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })