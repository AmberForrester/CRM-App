#10 - Create website/urls.py file.

from django.urls import path
from . import views #12 - Import views.

urlpatterns = [
    path('', views.home, name='home'), #11 - Create a new homepage.
    path('login/', views.login_user, name='login'), #28 - login url to views.py
    path('logout/', views.logout_user, name='logout'), #29 - logout url to views.py
]