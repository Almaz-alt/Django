from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('bathroom_products/', views.bathroom_products, name='bathroom_products'),
    path('kitchen_products/', views.kitchen_products, name='kitchen_products'),
    path('book/<int:id>/', views.book_detail_view, name='book_detail'),
    path('add_comment/<int:book_id>/', views.add_comment, name='add_comment'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('create_order/', views.create_order_view, name='create_order'),
    path('order_list/', views.order_list_view, name='order_list'),
]

