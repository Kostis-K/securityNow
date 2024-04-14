from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
#import requests

geia_sas_message = "GEIA SAS"
# Create your views here.
class StartView(APIView): #securityNow/hello
    def get(self, request, *args, **kwargs):
        print(geia_sas_message)
        return Response(geia_sas_message, status=status.HTTP_200_OK)
class EmployeeApiView(APIView): #securityNow/employee
    def post(self, request, *args, **kwargs):
        print("Post request called....!!!!! Up in here...!!")
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)