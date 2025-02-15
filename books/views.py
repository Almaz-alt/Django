from django.shortcuts import render
from .models import Clothing

def ClothingListView(request):
    category = request.GET.get('category', '')
    if category:
        clothes = Clothing.objects.filter(category=category)
    else:
        clothes = Clothing.objects.all()
    return render(request, 'products_home/clothing_list.html', {'clothes': clothes})
