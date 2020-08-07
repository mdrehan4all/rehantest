from rest_framework import serializers
from .models import members, activityperiods

class activityperiodsSerializer(serializers.ModelSerializer):
   
    class Meta:
       model = activityperiods
       #fields = '__all__'
       fields = ['mid', 'startime', 'endtime']

class membersSerializer(serializers.ModelSerializer):
   
    class Meta:
       model = members
       #fields = '__all__'
       fields = ['mid', 'realname', 'tz']
	   

	   