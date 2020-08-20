from django.urls import path
from . import views

urlpatterns =[
    path('',views.login),
    path('register/',views.register,name='register'),
    path('deployapplication/',views.deployapplication,name='deployapplication'),
]
