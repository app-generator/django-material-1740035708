# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Peptides(models.Model):

    #__Peptides_FIELDS__
    peptides = models.CharField(max_length=255, null=True, blank=True)
    hla = models.CharField(max_length=255, null=True, blank=True)
    donors = models.CharField(max_length=255, null=True, blank=True)
    ptm = models.CharField(max_length=255, null=True, blank=True)
    organ = models.CharField(max_length=255, null=True, blank=True)

    #__Peptides_FIELDS__END

    class Meta:
        verbose_name        = _("Peptides")
        verbose_name_plural = _("Peptides")


class Donor(models.Model):

    #__Donor_FIELDS__
    donor_id = models.CharField(max_length=255, null=True, blank=True)
    hla = models.CharField(max_length=255, null=True, blank=True)

    #__Donor_FIELDS__END

    class Meta:
        verbose_name        = _("Donor")
        verbose_name_plural = _("Donor")



#__MODELS__END
