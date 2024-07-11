# в файле urls.py вашего приложения
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users-list'),
    path('register/', views.register, name='register'),
    # Другие маршруты вашего приложения
]