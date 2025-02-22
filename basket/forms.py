from django import forms
from .models import CartItem, Order

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['book', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
