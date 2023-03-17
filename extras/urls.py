from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('service-detail/<int:pk>', views.view_service, name='view-service'),
    path('application-detail/<int:pk>', views.view_application, name='view-application'),

]
