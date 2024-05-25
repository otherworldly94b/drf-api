from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Bookmark(models.Model):
  """
  Bookmark model, related to 'owner' and 'bookmarked_post'.
  'owner' is a User instance and 'bookmarked_post' is a Post instance.
  'unique_together' makes sure a user can't bookmark the same post twice.
  """
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  bookmarked_post = models.ForeignKey(
      Post, related_name='bookmarks', on_delete=models.CASCADE
  )
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-created_at']
    unique_together = ['owner', 'bookmarked_post']

  def __str__(self):
    return f"{self.owner.username} bookmarked - {self.bookmarked_post.title}"
