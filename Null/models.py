from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    experience = models.IntegerField(default=0)  # Experience in years
    position = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.FloatField(default=0.0)
    linkedin = models.URLField(blank=True, null=True)
    year = models.PositiveIntegerField(default=1)
    salary = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if 1 <= self.year < 3:
            self.salary = 100
        elif 3 <= self.year < 8:
            self.salary = 200
        elif 8 <= self.year < 15:
            self.salary = 300
        else:
            self.salary = 400
        super().save(*args, **kwargs)