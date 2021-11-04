from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'signupmanager'

urlpatterns = [
    path('viewuser/', views.usersList),
    path('insertuser/', views.insertuser),
    path('viewdoctors/', views.viewdoctors),
]
