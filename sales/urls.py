from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product'),
    path('sales/', views.sale_list, name='sale_list'),
    path('create_sale/', views.create_sale, name='create_sale'),

]
