from django.conf import settings
from django.urls import reverse
import re
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        # print('PATH:', path)
        # print('EXEMPT_URLS:', EXEMPT_URLS)
        # print('REQUEST:', request)

        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        # trim off all leading characters in variable path, leaving the last 7 characters
        if path[-7:] == reverse('logout').lstrip('/'):
             logout(request)

        if request.user.is_authenticated() and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated() or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)