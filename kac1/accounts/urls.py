from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

from . import views

# the url at the end allows for redirecting default help_text URL for the password field in
# class EditProfileForm(UserChangeForm)
# url(r'^profile/password/$', views.change_password, name='change_password2'),

urlpatterns = [
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^$', TemplateView.as_view(template_name='accounts/home.html'), name='home'),
    url(r'^profile/password/$', views.change_password, name='change_password2'),
    url(r'^testMe/$', views.testMe, name='testMe'), ]

