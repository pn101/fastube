from django.db import models
from django.core.urlresolvers import reverse

from users.models import User


class Post(models.Model):

    user = models.ForeignKey(User)

    like_user_set = models.ManyToManyField(
            User,
            related_name='like_post_set',
            through='Like',
    )

    hash_id = models.CharField(
            max_length=8,
            blank=True,
            null=True,
    )

    video_id = models.CharField(
            max_length=16,
    )
    video_original_title = models.CharField(
            max_length=256,
            blank=True,
            null=True,
    )

    title = models.CharField(
            max_length=256,
    )
    content = models.TextField()

    def get_youtube_original_url(self):
        from posts.utils import get_youtube_original_url as get_youtube_original_url_from_youtube
        return get_youtube_original_url_from_youtube(self.video_id)
    youtube_original_url = property(get_youtube_original_url)

    def get_youtube_embed_url(self):
        from posts.utils import get_youtube_embed_url as get_youtube_embed_url_from_youtube
        return get_youtube_embed_url_from_youtube(self.video_id)
    youtube_embed_url = property(get_youtube_embed_url)

    def get_youtube_thumbnail_url(self):
        from posts.utils import get_youtube_thumbnail_url as get_youtube_thumbnail_url_from_youtube
        return get_youtube_thumbnail_url_from_youtube(self.video_id)
    youtube_thumbnail_url = property(get_youtube_thumbnail_url)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
                'posts:detail',
                kwargs={
                    'slug': self.hash_id,
                }
        )
