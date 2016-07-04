from django.views.generic import View

from posts.models import Post


class PostBaseView(View):
    model = Post
    slug_field = 'hash_id'
