from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from .models import members, activityperiods
from .serializers import membersSerializer, activityperiodsSerializer

'''
class memberList(APIView):
   
   def get(self, request):
       member1 = members.objects.all()
       activityperiods1 = activityperiods.objects.all()
       serializers = membersSerializer(member1, many = True)
       return Response(serializers.data)
	  
   def post(self):
      pass
# Create your views here.
'''

class memberList(viewsets.ModelViewSet):
    queryset = members.objects.all().order_by('-mid')
    serializer_class = membersSerializer


class activityperiodsList(viewsets.ModelViewSet):
    queryset = activityperiods.objects.all()
    serializer_class = activityperiodsSerializer