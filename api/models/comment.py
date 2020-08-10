from django.db import models

from .user import User
from .post import Post

class Comment(models.Model):
  body = models.CharField(max_length=140)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return self.body

  def as_dict(self):
    """Returns dictionary version of Comment models"""
    return {
        'id': self.id,
        'body': self.body,
    }
