from django.contrib import admin
from .models import BookModel, Review, Cart, CartItem, Order, OrderItem, Clothing

@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'price', 'created_at']
    list_filter = ['genre', 'created_at']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'name', 'created_at']
    list_filter = ['created_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    list_filter = ['created_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'book', 'quantity']
    list_filter = ['cart']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    list_filter = ['status', 'created_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'quantity']
    list_filter = ['order']

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description']
    list_filter = ['category']
