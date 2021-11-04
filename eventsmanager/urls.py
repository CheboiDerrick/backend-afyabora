from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'eventsmanager'

urlpatterns = [
    path('events/', views.eventsList),
    path('addevent/', views.addevent),
    path('editevent/', views.editevent),
    path('deleteevent/', views.deleteevent)
]
