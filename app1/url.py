from django.urls import path
from .views import homepage,page2,viewform,submitform

urlpatterns=[
    path('',homepage,name='homepage'),


    path('page2',page2,name='page2'),


    path('form',viewform,name='form'),

    path('submitform',submitform,name='submitform')



]

