"""Bookings URL Configuration

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
    path('api/booking/update_user_by_ID',views.update_user_by_ID),
    path('api/booking/all',views.list_all),
    path('api/booking/order',views.order),
    path('api/booking/add_user',views.add_user),
    path('api/booking/list_user',views.getlist_user),
    path('admin/', admin.site.urls),
]
