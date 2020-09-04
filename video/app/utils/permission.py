# coding:utf-8

import functools

from django.shortcuts import redirect, reverse
from app.model.auth import ClientUser
from .consts import COOKIE_NAME


def dashboard_auth(func):
    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('login'), request.path))

        return func(self, request, *args, **kwargs)

    return wrapper


def client_auth(request):
    value = request.COOKIES.get(COOKIE_NAME)
    print(value)
    if not value:
        return

    user = ClientUser.objects.filter(pk=value)
    print(user)
    if user:
        return user[0]
    else:
        return None
