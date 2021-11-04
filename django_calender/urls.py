"""django_calender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_event/',include('create_event.urls')),
    path('delete_event/',include('delete_event.urls')),
    path('eventsmanager/',include('eventsmanager.urls')),
    path('signupmanager/',include('signupmanager.urls' , namespace="signupmanager")),
    path('update_event/',include('update_event.urls')),
    path('usersmanager/',include('usersmanager.urls')),
]
