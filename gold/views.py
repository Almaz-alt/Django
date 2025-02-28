from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm, IngredientForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})


def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})


def ingredient_create(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk=recipe_pk)

    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = IngredientForm()

    return render(request, 'ingredient_form.html', {'form': form, 'recipe': recipe})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')
