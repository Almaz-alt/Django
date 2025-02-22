from django.db import models


class ParsedData(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('movie', 'Movie'),
        ('tv_show', 'TV Show'),
        ('book', 'Book'),
    ]

    title = models.CharField(max_length=200)
    link = models.URLField()
    summary = models.TextField()
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
