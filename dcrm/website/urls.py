#10 - Create website/urls.py file.

from django.urls import path
from . import views #12 - Import views.

urlpatterns = [
    path('', views.home, name='home'), #11 - Create a new homepage.
]