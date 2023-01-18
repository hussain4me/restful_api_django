from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from . serializer import employeeSerializer


class employeeList(APIView):

    def get(self, request):
        employeeList = employee.objects.all()

        serializer = employeeSerializer(employeeList, many=True)
        return Response(serializer.data)

    def post(self):
        pass


# Create your views here.
