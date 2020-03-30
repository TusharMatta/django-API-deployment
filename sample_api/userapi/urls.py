from django.urls import path
from userapi import views

urlpatterns = [
    path('', views.index),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('final/', views.user_view),
]
