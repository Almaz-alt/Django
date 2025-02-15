from django.urls import path
from .views import ClothingListView

urlpatterns = [
    path('clothing_list/', ClothingListView, name='clothing_list'),

]
