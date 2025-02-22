from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart, create_order_view, order_list_view

urlpatterns = [
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('create_order/', create_order_view, name='create_order'),
    path('order_list/', order_list_view, name='order_list'),
]
