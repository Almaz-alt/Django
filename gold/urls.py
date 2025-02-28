from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:recipe_pk>/ingredient/create/', views.ingredient_create, name='ingredient_create'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
]
