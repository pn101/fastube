from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class PostModelTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='username',
                password='password',
        )

        self.post_video_id = 'fastube'

        self.post = self.user.post_set.create(
                title='test_title',
                video_id=self.post_video_id,
        )

    def test_post_model_original_url(self):
        youtube_original_url = 'https://www.youtube.com/watch?v={post_video_id}'.format(
                post_video_id=self.post.video_id,
        )

        self.assertEqual(
                self.post.get_youtube_original_url(),
                youtube_original_url,
        )
        self.assertEqual(
                self.post.youtube_original_url,
                youtube_original_url,
        )

    def test_post_model_embed_url(self):
        youtube_embed_url = 'https://www.youtube.com/embed/{post_video_id}'.format(
                post_video_id=self.post.video_id,
        )

        self.assertEqual(
                self.post.get_youtube_embed_url(),
                youtube_embed_url,
        )
        self.assertEqual(
                self.post.youtube_embed_url,
                youtube_embed_url,
        )
