from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from product.models import Product, Category

from .forms import SignUpForm


def frontpage(request):
    """Главная страница сайта"""
    products = Product.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'products': products})


def signup(request):
    """Регистрация на сайте"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


@login_required
def my_account(request):
    """Профиль"""
    return render(request, 'core/myaccount.html')


@login_required
def edit_my_account(request):
    """Редактировать профиль"""
    if request.method == 'POST':

        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')


def shop(request):
    """Страница магазин"""
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category,
        }
    return render(request, 'core/shop.html', context)
