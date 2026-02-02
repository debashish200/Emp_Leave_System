from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('logout/', user_logout, name='logout'),
]

