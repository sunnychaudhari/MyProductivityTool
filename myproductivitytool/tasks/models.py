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
    user = models.ForeignKey(User,default=None, related_name='project_user', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=500, default=None, blank=False)

    class Meta:
        app_label = 'tasks'


class Task(models.Model):
    project = models.ForeignKey(Project,default=None, related_name='task_project', on_delete=models.CASCADE)
    task_name = models.CharField(max_length=500, default=None, blank=False)
    assigned_to = models.ForeignKey(User,default=None, related_name='assigned_user', blank=True, null=True, on_delete=models.CASCADE)
    prioriry = models.CharField(choices=PRIORITY,max_length=20, default='Disabled')
    due_date = models.DateField(default=None, blank=True, null=True)
    task_description = models.CharField(max_length=500, default=None, blank=True, null=True)
    complete = models.BooleanField(default=False)
    created_by = models.IntegerField (blank=True , null=True)
    created_at = models.DateTimeField (auto_now_add=True , auto_now=False)

    class Meta:
        app_label = 'tasks'
