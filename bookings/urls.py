from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('guest_detail/<int:id>',views.guest_detail,name='guest_detail'),
    path('handlerequest/',views.handlerequest,name='handlerequest')
]