from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
]