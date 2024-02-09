from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('our_rooms/',views.our_rooms,name='our_rooms'),

]