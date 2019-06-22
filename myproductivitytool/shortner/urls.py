from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^dashboard/',dashboard, name='dashboard_url'),
    url(r'^url_shortner/',url_shortner, name='short_url'),
]