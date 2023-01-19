from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog/', views.blog, name = 'blog'),
    path('product/', views.product, name = 'product'),
    path('blog_single/', views.blog_single, name = 'blog_single'),
    path('cart/', views.cart, name = 'cart'),
    path('contact/', views.contact, name = 'contact'),
    path('regular/', views.regular, name = 'regular'),
    path('shop/', views.shop, name = 'shop'),
]