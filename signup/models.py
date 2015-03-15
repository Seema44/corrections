from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

#class kiven(models.Model):
 #    kiven = models.CharField(max_length =200 , blank =True)
#     kithe_ho = models.CharField(max_length =200 , blank =True)
 #    ki_krde = models.CharField(max_length =200, blank =True)


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default="Dragons.")

    def __unicode__(self):
        return self.favorite_animal













                                                                                                                                               
                                       
