from django.db import models
from django.contrib.auth.models import AbstractUser
from .const import GENDER_CHOICES


class ExtendedUser(AbstractUser):
    """ Extend common django user fields"""

    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    about_me = models.CharField(max_length=2048, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='idk')
    interests_tags = models.ManyToManyField('InterestsTags', related_name='user_inter_tags', blank=True, null=True)
    own_interests = models.ManyToManyField('OwnInterests', related_name='user_own_inter', blank=True, null=True)


class InterestsTags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OwnInterests(models.Model):
    name = models.CharField(max_length=100)
    tag = models.ForeignKey(InterestsTags, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
