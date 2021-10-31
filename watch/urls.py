from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('cakes/', views.business, name='business'), 
    path('wines/', views.wines, name='wines'),
]