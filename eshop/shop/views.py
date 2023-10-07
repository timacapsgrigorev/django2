from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm
from django.utils import timezone
from datetime import timedelta

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


# Create
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

# Read
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client_detail.html', {'client': client})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})

# Update
def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def update_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'update_order.html', {'form': form})

# Delete
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect('client_list')

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product_list')

def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('order_list')

def index(request):
    context = {
        'welcome_message': 'Добро пожаловать в мой магазин!',
    }
    return render(request, 'shop/index.html', context)

def ordered_products_list(request, period):
    today = timezone.now()
    start_date = today - timedelta(days=period)

    orders = Order.objects.filter(
        client=request.user,
        created_at__gte=start_date,
    )

    products = Product.objects.filter(order__in=orders).distinct()

    context = {
        'products': products,
        'period': period,
    }

    return render(request, 'shop/ordered_products_list.html', context)


def all_orders(request):
    orders = Order.objects.filter(client=request.user).order_by('-created_at')

    context = {
        'orders': orders,
    }

    return render(request, 'shop/all_orders.html', context)

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'shop/client_detail.html', {'client': client})