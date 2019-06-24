# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

PRIORITY = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User,default=None, related_name='project_user')
    project_name = models.CharField(max_length=500, default=None, blank=False)

    class Meta:
        app_label = 'tasks'


class Task(models.Model):
    project = models.ForeignKey(Project,default=None, related_name='task_project')
    task_name = models.CharField(max_length=500, default=None, blank=False)
    prioriry = models.CharField(choices=PRIORITY,max_length=20, default='Disabled')
    due_date = models.DateField(default=None, blank=True, null=True)
    complete = models.BooleanField(default=False)

    class Meta:
        app_label = 'tasks'
