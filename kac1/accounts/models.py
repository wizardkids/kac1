from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#if you use a particular query a lot, it can be defined usine a UserProfileManager
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    email = models.EmailField()

    #the following line makes sure that implementation of class UserProfile
    #instantiates the UserProfileManager
    #london = UserProfileManager()


    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
