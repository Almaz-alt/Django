from django.db import models
from django.conf import settings

class BookModel(models.Model):
    GENRE_CHOICE = (
        ('fantasy', 'Fantasy'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('sci-fi', 'Sci-Fi'),
        ('non-fiction', 'Non-fiction'),
    )
    image = models.ImageField(upload_to='books/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICE)
    email = models.EmailField()
    author = models.CharField(max_length=100)
    trailer = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

class Review(models.Model):
    book = models.ForeignKey('BookModel', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Clothing(models.Model):
    CATEGORY_CHOICES = (
        ('kids', 'Детская'),
        ('teens', 'Подростковая'),
        ('adults', 'Взрослая'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='clothes/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} - {self.user.username}"

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    book = models.ForeignKey('BookModel', on_delete=models.CASCADE, related_name='cart_books')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} (x{self.quantity})"

    def get_total_price(self):
        return self.quantity * self.book.price

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('canceled', 'Canceled'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username} ({self.status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    book = models.ForeignKey('BookModel', on_delete=models.CASCADE, related_name='order_books')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} (x{self.quantity})"
