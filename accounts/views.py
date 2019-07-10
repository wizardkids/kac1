from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import RegistrationForm, EditProfileForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from . import models


def home(request):
    return render(request, reverse('accounts:home'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg-form.html', args)


def view_profile(request, pk = None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    # print('REVERSE:', reverse('accounts:view_profile'))
    return render(request, 'accounts/view-profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view-profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit-profile.html', args)


def change_password(request):
    """
    Source: https://stackoverflow.com/questions/5802189/django-errno-111-connection-refused
    Requires an email server. For testing purposes:
        1. Settings:
            EMAIL_HOST = 'localhost'
            EMAIL_PORT = 1025
        2. python -m smtpd -n -c DebuggingServer localhost:1025
    """
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view-profile'))
        else:
            return redirect(reverse('accounts:change-password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change-password.html', args)


def testMe(request):
    user_data = models.User.objects.all()
    t = user_data
    r = request
    return render(request, 'accounts/testMe.html', {"entry": t, 'r': r})
