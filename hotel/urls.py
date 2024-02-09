"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views as home_views
from room import views as room_views
from user import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('home/', include('home.urls')),
    path('room/',include('room.urls')),
    path('bookings/',include('bookings.urls')),
    path('user/',include('user.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('about/',home_views.about,name='about'),
    path('contact/',home_views.contact,name='contact'),
    path('room/<int:id>/<slug:slug>',home_views.room_details,name='room_details'),
    path('search/',home_views.search,name='search'),

    path('login/',user_views.login_form,name='login_form'),
    path('logout/',user_views.logout_func,name='logout_func'),
    path('signup/',user_views.signup_form,name='signup_form'),


]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)