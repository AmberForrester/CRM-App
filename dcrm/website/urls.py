#10 - Create website/urls.py file.

from django.urls import path
from . import views #12 - Import views.

urlpatterns = [
    path('', views.home, name='home'), #11 - Create a new homepage.
    # path('login/', views.login_user, name='login'), #28 - login url to views.py if you want your own login page created.
    path('logout/', views.logout_user, name='logout'), #29 - logout url to views.py
    path('register/', views.register_user, name='register'), #43 - Register url
    path('record/<int:pk>', views.customer_record, name='record'), #81 - New path for records by passing an integer as a primary key. For example: localhost:8000/record/2 and that 2 will represent the primary key that we will pass into the view, and take it to pump into the DB and have it return the record corresponding.
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'), #94 - Delete button still passing the primary key to know which record to delete.
    path('add_record/', views.add_record, name='add_record'), #97 - Add record link to views.py file
]