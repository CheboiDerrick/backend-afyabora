from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from create_event import *

@api_view(['GET, POST'])
def index(request):
        if request.method == 'GET':

                return HttpResponse ()



