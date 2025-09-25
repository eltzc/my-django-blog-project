# blog/urls.py
from django.urls import path
from . import views # Импортируем views из текущего приложения

urlpatterns = [
    path('', views.blog_index, name='blog_index'), # Главная страница
    path('post/<slug:post_slug>/', views.blog_detail, name='blog_detail'), # Детальная страница поста
    path('set-preference/', views.set_preference, name='set_preference'), # Обработка настроек
]