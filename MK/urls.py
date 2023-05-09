from django.contrib import admin
from django.urls import path
from MK import views

urlpatterns = [
  path("",views.index,name='MK'),
  path("about",views.about,name='about'),
  path("services",views.services,name='services'),
  path("callout",views.callout,name='callout'),
  path("portfolio",views.portfolio,name='portfolio'),
]