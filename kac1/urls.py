"""Kids Athlete Club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/password-reset/$', auth_views.password_reset,
        {'template_name': 'accounts/registration/password-reset.html',
         'post_reset_redirect': 'password_reset_done',
         'email_template_name': 'accounts/registration/password-reset-email.html'},
        name='password_reset'),
    url(r'^accounts/registration/password-reset/done/$', auth_views.password_reset_done,
        {'template_name': 'accounts/registration/password-reset-done.html'},
        name='password_reset_done'),
    url(r'^admin/password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,
        {'template_name': 'accounts/registration/password-reset-confirm.html',
            'post_reset_redirect': 'password_reset_complete'},
        name='password_reset_confirm'),
    url(r'^accounts/registration/password-reset/complete/$', auth_views.password_reset_complete,
        {'template_name': 'accounts/registration/password-reset-complete.html'},
        name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# url(r'^accounts/login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
