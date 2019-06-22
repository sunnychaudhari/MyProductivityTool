# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import *
import random
import string

# Create your views here.
def dashboard(request):
    return render(request , 'url_shortner_dashboard.html' , {})

@csrf_exempt
def url_shortner(request):
    """
    Api for url shortner

    :return: Json response to convert the url
    """
    if request.method == 'POST':
        input_url = request.POST.get('input_url','')
        if input_url:
            url_obj = Urlshortner.objects.filter(original_url=input_url).last()
            if not url_obj:
                lettersAndDigits = string.ascii_letters + string.digits
                unique_id = ''.join(random.choice(lettersAndDigits) for i in range(5))
                url_obj = Urlshortner.objects.create(original_url=input_url, uid=unique_id)

    url_shortner = "http://localhost:8000/"+str(url_obj.uid)
    context = {'url_shortner': url_shortner}
    return JsonResponse(context, safe=False)


def original_url(request, uid):
    if uid:
        url_obj = Urlshortner.objects.filter(uid=str(uid)).last()
        if url_obj:
            original_url = url_obj.original_url
            return redirect(original_url)
    return HttpResponseNotFound ("Resource Not found")
