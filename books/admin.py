from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.BookModel)  # Исправлено: models.BookModel
class BookModelAdmin(admin.ModelAdmin):  # Исправлено: BookModelAdmin
    list_display = ['title', 'author', 'genre', 'price', 'created_at']
    list_filter = ['genre', 'created_at']
    search_fields = ['title', 'author', 'genre']

@admin.register(models.Review)  # Исправлено: models.Review
class ReviewAdmin(admin.ModelAdmin):  # Исправлено: ReviewAdmin
    list_display = ['book', 'rating', 'created_at']  # Исправлено: 'rating' вместо 'stars'
    list_filter = ['rating', 'created_at']  # Исправлено: 'rating' вместо 'start'
    search_fields = ['book__title']  # Изменено: по 'book__title' для поиска по названию книги
