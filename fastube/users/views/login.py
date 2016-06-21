from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/login.html',
                {
                    'site_name': 'Login Page',
                }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next_page') or ('user:mypage')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            messages.add_message(
                    request,
                    messages.SUCCESS,
                    settings.LOGIN_SUCCESS_MESSAGE,
            )

            return redirect(next_page)

        messages.add_message(
                request,
                messages.ERROR,
                settings.LOGIN_ERROR_MESSAGE,
        )
        return redirect('user:login')
