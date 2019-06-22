# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Urlshortner(models.Model):
    original_url = models.CharField(max_length=200, default=None, blank=False, unique=True)
    uid = models.CharField(max_length=200, default=None, blank=False)

    class Meta:
        app_label = 'shortner'