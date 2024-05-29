from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Dislike(models.Model):
    """
    Dislike model, related to 'owner' and 'dislike_post'.
    'owner' is a User instance and 'dislike_post' is a Post instance.
    'unique_together' makes sure a user can't dislike the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    dislike_post = models.ForeignKey(
        Post, related_name='dislikes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'dislike_post']

    def __str__(self):
        return f'{self.owner} {self.dislike_post}'