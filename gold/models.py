from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.quantity}"
