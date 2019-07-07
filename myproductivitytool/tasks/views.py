# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseNotFound, QueryDict
from .models import Project, Task
import datetime
import json
# Create your views here.
# @csrf_exempt
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/project/')

    return render(request, 'login.html', {})


def logout_page(request):
    logout (request)
    return redirect ('login')

@login_required
@csrf_exempt
def project_page(request):
    if request.method == 'POST':
        context = {}
        user_id = request.POST.get('user_id','')
        project_name = request.POST.get('project_name','')
        if user_id and project_name:
            proj_obj = Project.objects.create(user_id=user_id, project_name=project_name)
            context = {'id': proj_obj.id,'user_id': user_id, 'project_name': project_name}
        return JsonResponse(context, safe=False)
    if request.method == 'PATCH':
        context = {}
        data = QueryDict(request.body)
        project_id = data['project_id']
        project_name = data['project_name']
        if project_id and project_name:
            Project.objects.filter(id=int(project_id)).update(project_name=str(project_name))
            context = {'id': project_id, 'project_name': project_name}
        return JsonResponse(context, safe=False)
    if request.method == 'DELETE':
        context = {}
        data = QueryDict(request.body)
        project_id = data['project_id']
        if project_id:
            Project.objects.filter(id=int(project_id)).delete()
        return JsonResponse(context, safe=False)
    else:
        proj_obj = Project.objects.filter(user_id=request.user.id).values()
        context = {'project': list(proj_obj)}
        return render(request, 'project.html', context)


@login_required
@csrf_exempt
def task_page(request):
    if request.method == 'POST':
        context = {}
        task_name = request.POST.get('task_name','')
        project_id = request.POST.get('project_id','')
        user_id = request.user.id
        if user_id and task_name and project_id:
            task_obj = Task.objects.create(project_id=project_id, task_name=task_name, created_by=user_id)
            context = {'id': task_obj.id, 'assigned_to':task_obj.assigned_to, 'due_date':task_obj.due_date,
                       'task_name': task_obj.task_name,'project_id': int(task_obj.project_id)}
        return JsonResponse(context, safe=False,status=201)
    if request.method == 'PATCH':
        context = {}
        data = QueryDict(request.body)
        task_id = data['task_id']
        task_name = data['task_name']
        if task_id and task_name:
            Task.objects.filter(id=int(task_id)).update(task_name=str(task_name))
        return JsonResponse(context, safe=False, status=200)
    if request.method == 'DELETE':
        context = {}
        data = QueryDict(request.body)
        task_id = data['task_id']
        if task_id:
            Task.objects.filter(id=int(task_id)).delete()
        return JsonResponse(context, safe=False, status=200)
    else:
        context = {}
        # proj_obj = Project.objects.all().values()
        # context = {'project': list(proj_obj)}
        return render(request, 'project.html', context)


@login_required
@csrf_exempt
def update_task_details(request):
    if request.method == 'PATCH':
        context = {}
        data = QueryDict(request.body)
        task_id = data['task_id']
        task_assigned_to = data[ 'task_assigned_to' ]
        task_due_date = data[ 'task_due_date' ]
        task_description = data[ 'task_description' ]
        if task_due_date:
            task_due_date = datetime.datetime.strptime(str(task_due_date), "%m/%d/%Y").strftime("%Y-%m-%d")

        if task_id:
            Task.objects.filter(id=int(task_id)).update(
                assigned_to=int(task_assigned_to), due_date=task_due_date, task_description=str(task_description)
            )
            context = {
                'assigned_to': int (task_assigned_to) , 'due_date': task_due_date ,
                'task_description': str (task_description)
            }
        return JsonResponse(context, safe=False, status=200)

@login_required
def project_details_page(request, project_id):
    proj_obj = Project.objects.filter(id=project_id,user_id=request.user.id)
    tasks = Task.objects.filter(project_id=project_id).order_by('id')
    users = list(User.objects.all().values('id','username'))
    if proj_obj:
        return render(request, 'task.html', {'project': proj_obj.last(), 'tasks': tasks, 'users':users})
    else:
        return HttpResponseNotFound("Sorry, you dont have access to this resourse")



def signup_page(request):
    context_data = {}
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password', '')
        if username and password and (password == confirm_password):
            try:
                User.objects.create_user(username=username, password=password, is_active=True)
                return redirect('/login/')
            except:
                context_data = {'error': 'User with this username already exists'}
        else:
            context_data = {'error': 'Something went wrong, please try again'}

    return render(request, 'signup.html', context_data)

