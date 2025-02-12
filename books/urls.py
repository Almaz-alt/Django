from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('photo/', views.text_and_photo, name='text_and_photo'),
    path('time/', views.system_time, name='system_time'),
    path('book_list/', views.book_list_view, name='book_list'),  # добавил путь для списка книг
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),  # исправлено
]

