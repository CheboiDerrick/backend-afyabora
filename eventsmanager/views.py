from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import json
from django.forms.models import model_to_dict
from rest_framework.request import Request
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import events
from .serializers import eventsSerializer
from .serializers import aeventsSerializer
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse

@api_view(['POST', 'GET'])
def eventsList(request):
	rcvtype = request.data["utype"]
	rcvuid = request.data["uid"]

	if rcvtype ==1:
		eventsd = events.objects.filter(pid = rcvuid)
	elif rcvtype == 2:
		eventsd = events.objects.filter(did = rcvuid)
	serializer = aeventsSerializer(eventsd, many=True)
	return Response(serializer.data)


def index(request):
        return HttpResponse("Welcome to AfyaBoraClinic")


@api_view(['POST', 'GET'])
def addevent(request):
        serializer =  eventsSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()

        return Response(serializer.data)


@api_view(['POST', 'GET'])
def editevent(request):
        eventid = request.data["id"]
        event = events.objects.get(id = eventid)
        serializer =  eventsSerializer(instance = event, data = request.data)
        if serializer.is_valid():
                serializer.save()

        return Response(serializer.data)

@api_view(['POST', 'GET'])
def deleteevent(request):
        eventid = request.data["id"]
        event = events.objects.get(id = eventid)
        event.delete()
        return Response(-1)
