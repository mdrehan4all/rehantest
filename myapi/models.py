from django.db import models

# Create your models here.
class members(models.Model):
   mid = models.CharField(max_length=30)
   realname = models.CharField(max_length=30)
   tz = models.CharField(max_length=30)
   
   def __str__(self):
      return self.mid
	  
class activityperiods(models.Model):
   mid = models.CharField(max_length=30)
   startime = models.CharField(max_length=30)
   endtime = models.CharField(max_length=30)
   
   def __str__(self):
      return self.mid