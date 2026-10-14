
from django.shortcuts import render, get_object_or_404
from .models import Product,Banner,Category
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required




def home(request):
    products = Product.objects.filter(is_active=True)
    banners = Banner.objects.filter(is_active=True)
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        products = products.filter(category_id=category_id)

    return render(request, 'store/home.html', {
        'products': products,
        'banners': banners,
        'categories': categories,
    })



def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True
    )

    return render(request, 'store/product_detail.html', {
        'product': product
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
    else:
        form = UserCreationForm()

    return render(request, 'store/register.html', {
        'form': form
    })


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            login(request, form.get_user())
            return redirect('account')
    else:
        form = AuthenticationForm()

    return render(request, 'store/login.html', {
        'form': form
    })


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def account(request):
    return render(request, 'store/account.html')
