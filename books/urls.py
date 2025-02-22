from django.urls import path
from .views import ClothingListView, BookDetailView, AddCommentView, AddToCartView, CartDetailView, RemoveFromCartView, CreateOrderView, OrderListView

urlpatterns = [
    path('clothing_list/', ClothingListView.as_view(), name='clothing_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('add_comment/<int:book_id>/', AddCommentView.as_view(), name='add_comment'),
    path('add_to_cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart_detail/', CartDetailView.as_view(), name='cart_detail'),
    path('remove_from_cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
]

from django.urls import path
from .views import BookSearchView

urlpatterns += [
    path('search/', BookSearchView.as_view(), name='book_search'),
]

