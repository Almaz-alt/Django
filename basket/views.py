from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import BookModel, Review, Cart, CartItem, Order, OrderItem
from .forms import ReviewForm, OrderForm, CartItemForm

def all_products(request):
    query = BookModel.objects.all().order_by('-id')
    context = {'all_products': query}
    return render(request, 'products_home/all_products.html', context=context)

def bathroom_products(request):
    query = BookModel.objects.filter(tags__name='для ванной комнаты').order_by('-id')
    context = {'bathroom': query}
    return render(request, 'products_home/bathroom.html', context=context)

def kitchen_products(request):
    query = BookModel.objects.filter(tags__name='для кухни').order_by('-id')
    context = {'kitchen': query}
    return render(request, 'products_home/kitchen.html', context=context)

def book_detail_view(request, id):
    book = get_object_or_404(BookModel, id=id)
    comments = Review.objects.filter(book=book).order_by('-created_at')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_detail', id=book.id)
    else:
        form = ReviewForm()
    return render(request, 'book_detail.html', {'book': book, 'comments': comments, 'form': form})

def add_comment(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(BookModel, id=book_id)
        name = request.POST.get('name')
        text = request.POST.get('text')
        comment = Review.objects.create(book=book, name=name, text=text)
        response_data = {'name': comment.name, 'text': comment.text, 'date': comment.created_at.strftime("%Y-%m-%d %H:%M:%S")}
        return JsonResponse(response_data)

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
