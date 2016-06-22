from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'

    def ready(self):
        from posts.signals.post_save import post_save_post
