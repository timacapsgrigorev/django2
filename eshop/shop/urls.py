from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client/create/', views.create_client, name='create_client'),
    path('client/list/', views.client_list, name='client_list'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/<int:client_id>/update/', views.update_client, name='update_client'),
    path('client/<int:client_id>/delete/', views.delete_client, name='delete_client'),

    path('product/create/', views.create_product, name='create_product'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/update/', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    path('order/create/', views.create_order, name='create_order'),
    path('order/list/', views.order_list, name='order_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
]

