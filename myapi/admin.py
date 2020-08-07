from django.contrib import admin
from . models import members
from . models import activityperiods

# Register your models here.
admin.site.register(members)
admin.site.register(activityperiods)