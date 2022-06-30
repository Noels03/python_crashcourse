from django.contrib import admin

# Register your models here.

from .models import Topic

#####tells Django to manage our model through admin site####
admin.site.register(Topic)