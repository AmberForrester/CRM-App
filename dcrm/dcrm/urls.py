from django.contrib import admin
from django.urls import path, include #8 - import include.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), #9 - include path to new app. 
]
