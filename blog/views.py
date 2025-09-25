from django.shortcuts import render

# blog/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings # Для доступа к настройкам проекта

from .data import BLOG_POSTS, AVAILABLE_THEMES, AVAILABLE_LANGUAGES # Импортируем данные

def get_current_theme(request):
    """Получает тему из cookies или возвращает тему по умолчанию."""
    return request.COOKIES.get('theme', settings.DEFAULT_THEME) # Используем настройки проекта

def get_current_language(request):
    """Получает язык из cookies или возвращает язык по умолчанию."""
    return request.COOKIES.get('language', settings.DEFAULT_LANGUAGE)

def blog_index(request):
    """Главная страница блога."""
    posts = BLOG_POSTS
    current_theme = get_current_theme(request)
    current_language = get_current_language(request)

    context = {
        'posts': posts,
        'current_theme': current_theme,
        'current_language': current_language,
        'available_themes': AVAILABLE_THEMES,
        'available_languages': AVAILABLE_LANGUAGES
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, post_slug):
    """Страница детального просмотра статьи."""
    post = get_object_or_404(BLOG_POSTS, lambda p: p['slug'] == post_slug)
    current_theme = get_current_theme(request)
    current_language = get_current_language(request)

    context = {
        'post': post,
        'current_theme': current_theme,
        'current_language': current_language,
        'available_themes': AVAILABLE_THEMES,
        'available_languages': AVAILABLE_LANGUAGES
    }
    return render(request, 'blog/detail.html', context)

def set_preference(request):
    """Обработка POST запроса для сохранения настроек."""
    if request.method == 'POST':
        theme = request.POST.get('theme')
        language = request.POST.get('language')

        response = HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('blog_index'))) # Перенаправляем обратно

        if theme and theme in AVAILABLE_THEMES:
            response.set_cookie('theme', theme, max_age=3600 * 24 * 30) # Сохраняем на 30 дней
        if language and language in AVAILABLE_LANGUAGES:
            response.set_cookie('language', language, max_age=3600 * 24 * 30)

        return response
    else:
        # Если это GET запрос, просто перенаправляем на главную
        return HttpResponseRedirect(reverse('blog_index'))

# Вспомогательная функция для get_object_or_404 с нашим списком словарей
def get_object_or_404(data_list, condition_func):
    for item in data_list:
        if condition_func(item):
            return item
    from django.http import Http404
    raise Http404("Object not found")