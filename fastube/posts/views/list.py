from django.views.generic.list import ListView

from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['site_name'] = 'Post List'
        return context
