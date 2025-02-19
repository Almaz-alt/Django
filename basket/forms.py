from django import forms
from .models import Review, Order

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'content', 'rating']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'total_price']
from django import forms
from .models import Review, Order, CartItem

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'content', 'rating']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['book', 'quantity']
