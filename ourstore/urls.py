from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('home', homepage, name='home'),
    path('arrival', arrivals_page, name='arrivals'),
    path('store', store_page, name='store'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Updated pattern
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('about', about, name='about'),
    
]