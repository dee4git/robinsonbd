from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('all-product-view/', views.view_all_products, name='view-all-products'),
    path('product-detail/<int:pk>', views.view_product, name='view-product'),

]
