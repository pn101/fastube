from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                'user/signup.html',
                {
                    'site_name': 'Signup Page',
                }
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')

        # TODO: validations (username)

        user = get_user_model().objects.create_user(
                username=username,
                password=password,
                email=email,
                phonenumber=phonenumber,
        )
        # TODO: flash messages (success, error message)

        return redirect('user:login')
