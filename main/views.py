from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

def book_list_view(request):
    if request.method == "GET":
        query = models.Bookmodel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book.html', context=context_object_name)

def book_detail_view(request, id):
    if request.method == "GET":
        query = get_object_or_404(models.Bookmodel, id=id)
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book_detail.html', context=context_object_name)

def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут алмаз я учусь в 74 школе мне 14 лет")

def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse('<h1> 1970 Cadillac DeVille Classic Auto Mall</h1>')
