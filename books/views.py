from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BookModel, Review, Cart, CartItem, Order, OrderItem, Clothing
from .forms import ReviewForm, OrderForm, CartItemForm

class ClothingListView(ListView):
    model = Clothing
    template_name = 'clothing_list.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        category = self.request.GET.get('category', '')
        if category:
            return Clothing.objects.filter(category=category)
        return Clothing.objects.all()

class BookDetailView(DetailView):
    model = BookModel
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Review.objects.filter(book=self.object).order_by('-created_at')
        context['form'] = ReviewForm()
        return context

class AddCommentView(CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.book = get_object_or_404(BookModel, id=self.kwargs['book_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['book_id']})

class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    form_class = CartItemForm

    def form_valid(self, form):
        book = get_object_or_404(BookModel, id=self.kwargs['book_id'])
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, defaults={'quantity': 1})
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart_detail')

class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

    def get_object(self, queryset=None):
        return get_object_or_404(Cart, user=self.request.user)

class RemoveFromCartView(LoginRequiredMixin, DeleteView):
    model = CartItem

    def get_success_url(self):
        return reverse_lazy('cart_detail')

class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'create_order.html'
    success_url = reverse_lazy('order_list')

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class BookSearchView(ListView):
    model = BookModel
    template_name = 'book_search.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return BookModel.objects.filter(title__icontains=query)
        return BookModel.objects.all()
