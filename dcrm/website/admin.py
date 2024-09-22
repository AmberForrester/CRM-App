from django.contrib import admin

#70 - import the Model created in website/models.py file.
from .models import Record

#71 - Register this on the Admin section. 
admin.site.register(Record)
