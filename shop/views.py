from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse # Для генерации URL-адресов по их именам
from django.views.decorators.http import require_POST # Декоратор, разрешающий только POST-запросы
from django.views.generic import TemplateView # Базовый класс для простых страниц с шаблоном
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Для пагинации
from django.core.mail import send_mail # Для отправки email
from django.conf import settings # Для доступа к настройкам проекта
from django.db.models import Q # Для создания сложных поисковых запросов (OR-условия)
from django.utils import timezone # Для работы с временем (например, для купонов)
from django.contrib import messages # Для отображения флеш-сообщений пользователю

from .models import Product, Category # Модели данных


# --- Информационные страницы (используют Class-Based View - TemplateView) ---


# --- Представления для Корзины и Купонов ---

# Представление для добавления товара в корзину.

# Представление для удаления товара из корзины.

# Представление для отображения страницы с деталями корзины.

# Представление для применения купона к корзине.

# --- Представления для Каталога товаров ---

# Представление для отображения списка товаров (главная страница каталога, категории, результаты поиска).
def product_list(request, category_slug=None):
    category = None # Текущая категория (None, если не выбрана)
    categories = Category.objects.all() # Все категории для отображения в сайдбаре
    products_queryset = Product.objects.filter(available=True).order_by('name') # Начальный QuerySet всех доступных товаров
    
    # Фильтрация по категории, если передан category_slug
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_queryset = products_queryset.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products_queryset, # Передаем объект Page (не просто список) в шаблон
    }
    return render(request, 'shop/product/list.html', context)

# Представление для отображения детальной информации о товаре.

# --- Представления для Заказов ---

# Представление для создания (оформления) заказа.

# Представление для страницы "Спасибо за заказ" (подтверждение заказа).
