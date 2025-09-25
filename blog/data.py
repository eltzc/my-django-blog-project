# blog/data.py

# Пример списка статей
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Привет, мир Django!',
        'slug': 'hello-world-django',
        'content': 'Добро пожаловать на нашу платформу для блогов! Здесь мы будем делиться интересными статьями о Django и веб-разработке.',
        'author': 'Admin',
        'created_at': '2023-10-26',
        'theme': 'light', # Тема по умолчанию
        'language': 'ru'  # Язык по умолчанию
    },
    {
        'id': 2,
        'title': 'Настройка виртуального окружения',
        'slug': 'setting-up-venv',
        'content': 'Подробное руководство по созданию и активации виртуальных окружений для изоляции проектов.',
        'author': 'Developer',
        'created_at': '2023-10-27',
        'theme': 'dark',
        'language': 'en'
    },
    {
        'id': 3,
        'title': 'Работа с базами данных в Django',
        'slug': 'django-databases',
        'content': 'Основы работы с моделями, миграциями и запросами в Django ORM.',
        'author': 'Admin',
        'created_at': '2023-10-28',
        'theme': 'light',
        'language': 'ru'
    }
]

# Пример словаря для хранения настроек (например, тем)
# В реальном приложении это было бы более сложно, но для примера подходит
AVAILABLE_THEMES = {
    'light': 'Светлая тема',
    'dark': 'Темная тема',
    'blue': 'Синяя тема'
}

AVAILABLE_LANGUAGES = {
    'ru': 'Русский',
    'en': 'English'
}