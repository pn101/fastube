from django.db import models

from users.models import User


class Comment(models.Model):

    post = models.ForeignKey('Post')
    user = models.ForeignKey(User)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
