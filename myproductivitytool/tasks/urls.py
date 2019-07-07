from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^login/',login_page, name='login'),
    url(r'^signup/',signup_page, name='signup'),
    url(r'^tasks/',task_page, name='task_page'),
    url(r'^update_tasks/',update_task_details, name='update_task_details'),
    url(r'^project/$',project_page, name='project_page'),
    url(r'^api/project/$',project_page, name='project_create'),
    url(r'^project/(?P<project_id>\d+)/',project_details_page, name='project_details_page'),
]