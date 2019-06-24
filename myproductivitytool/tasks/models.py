# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User,default=None, related_name='project_user')
    project_name = models.CharField(max_length=500, default=None, blank=False)

    class Meta:
        app_label = 'tasks'

