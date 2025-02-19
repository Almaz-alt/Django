from django.contrib import admin
from .models import BookModel, Review, Cart, CartItem, Order, OrderItem

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'price', 'created_at']
    list_filter = ['genre', 'created_at']
    search_fields = ['title', 'author', 'genre']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['book__title']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'book', 'quantity']
    list_filter = ['cart']
    search_fields = ['book__title']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'status']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity']
    list_filter = ['order']
    search_fields = ['book__title']
