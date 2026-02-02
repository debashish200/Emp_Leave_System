from django.urls import path
from .views import *


urlpatterns = [
    path('request/',leave_request,name='leave_request'),
    path('approval/',approve_leave,name='approve_leave'),

    path('calendar/', leave_calendar, name='leave_calendar'),
    path('calendar/events/',leave_events, name='leave_events'),
]