from django.views.generic import View
from django.shortcuts import redirect


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return redirect('posts:list')
