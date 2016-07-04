from django.contrib.auth.models import AbstractUser
from django.db import models

from .follow import Follow


class User(AbstractUser):

    phonenumber = models.CharField(
            max_length=16,
            blank=True,
            null=True,
    )

    follower_set = models.ManyToManyField(
            'self',
            symmetrical=False,
            related_name='following_set',
            through=Follow,
            through_fields=('following', 'follower'),
    )
