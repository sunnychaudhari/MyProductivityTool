# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect

# Create your views here.
def dashboard(request):
    return render(request , 'url_shortner_dashboard.html' , {})

def url_shortner(request):
    """
    Api for url shortner

    :return: Json response to convert the url
    """
    if request.method == 'GET':
        print ""
    context = {}
    return JsonResponse(context, safe=False)
