from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import redirect


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you, come again',
        )
        return redirect('user:login')
