from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.home, name='home'),
    path('business/', views.business, name='business'), 
    path('wines/', views.wines, name='wines'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)