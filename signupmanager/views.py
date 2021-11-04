import json
from django.forms.models import model_to_dict
from rest_framework.request import Request
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import userdata
from .serializers import usersSerializer
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse


@api_view(['POST', 'GET'])
def usersList(request):
	rcvemail = request.data["email"]
	rcvpwd = request.data["password"]
	try:
		userd = userdata.objects.get(email = rcvemail, password = rcvpwd)
	except userdata.DoesNotExist:
		userd = None
	serializer = usersSerializer(userd, many=False)
	return Response(serializer.data)

@api_view(['POST', 'GET'])
def insertuser(request):
	serializer =  usersSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST', 'GET'])
def viewdoctors(request):
        try:
                userd = userdata.objects.filter(utype = 1)
        except userdata.DoesNotExist:
                userd = None
        serializer = usersSerializer(userd, many=True)
        return Response(serializer.data)

