from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import BookModel, Cart, CartItem, Order, OrderItem
from .forms import CartItemForm, OrderForm

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(BookModel, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def create_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

@login_required
def order_list_view(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})
