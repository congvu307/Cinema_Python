"""Catalogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from api import views
urlpatterns = [
    path('api/catalog/schedule/list',views.getlist_schedule),
    path('api/catalog/schedule/movie/<str:movie_ID>',views.schedule_by_movieID),
    path('api/catalog/schedule/add',views.add_schedule),
    path('api/catalog/cinema_room/list',views.getlist_cinemaRoom),
    path('api/catalog/cinema_room/add',views.add_cinemaRoom),
    path('api/catalog/city/add',views.add_city),
    path('api/catalog/city/list',views.getlist_city),
    path('admin/', admin.site.urls),
]
