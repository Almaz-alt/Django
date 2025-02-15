from django.db import models

class Clothing(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='clothes/')

    def __str__(self):
        return self.name

# Другие модели, например BookModel и Review
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
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
