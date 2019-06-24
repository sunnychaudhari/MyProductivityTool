# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseNotFound, QueryDict
from .models import Project

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
    else:
        proj_obj = Project.objects.all().values()
        context = {'project': list(proj_obj)}
        return render(request, 'project.html', context)

@login_required
def project_details_page(request, project_id):
    proj_obj = Project.objects.filter(id=project_id,user_id=request.user.id)
    if proj_obj:
        return render(request, 'task.html', {'project': proj_obj.last()})
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

