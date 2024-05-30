from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bookmarks.models import Bookmark
from dislikes.models import Dislike


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model instances.
    Includes owner information, profile details,
    and computed fields like like/bookmark/dislike counts,
    and IDs for the current user's
    interactions (if authenticated).
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    bookmark_id = serializers.SerializerMethodField()
    bookmarks_count = serializers.ReadOnlyField()
    dislike_id = serializers.SerializerMethodField()
    dislikes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Image validation to ensure it is under 2MB in size and
        does not exceed 4096px in width or height.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_bookmark_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, bookmark_post=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    def get_dislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dislike = Dislike.objects.filter(
                owner=user, dislike_post=obj
            ).first()
            return dislike.id if dislike else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'bookmark_id',
            'bookmarks_count', 'comments_count',
            'dislike_id', 'dislikes_count'
        ]
