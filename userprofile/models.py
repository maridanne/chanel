from django.contrib.auth.models import User
from django.db import models
from lib2to3.pytree import Base
from statistics import mode
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import DesignerProduct



class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofiles', on_delete=models.CASCADE)

    def __str__(self):
	    return self.user.username
