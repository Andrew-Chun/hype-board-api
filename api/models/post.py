from django.db import models

from .user import User

# Create your models here.
class Post(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  body = models.CharField(max_length=140)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  owner = models.ForeignKey(
      User,
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Title:'{self.title}' Body: {self.body} created_at: {self.created_at} updated_at: {self.updated_at}"

  def as_dict(self):
    """Returns dictionary version of Post models"""
    return {
        'id': self.id,
        'title': self.title,
        'body': self.body,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
        'owner': self.owner,
        'comment': self.comment
    }
