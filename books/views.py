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
        return render(request, 'book.html', context=context_object_name)


def book_detail_view(request, id):
    if request.method == "GET":
        query = get_object_or_404(models.Bookmodel, id=id)
        context_object_name = {
            'book': query,
        }
        return render(request, 'book_detail.html', context=context_object_name)


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Алмаз, я учусь в 74 школе, мне 14 лет.")


def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse('<h1> 1970 Cadillac DeVille Classic Auto Mall</h1>'
                            '<img src="https://bringatrailer.com/wp-content/uploads/2022/10/1970_cadillac_coupe-deville_1970_cadillac_coupe-deville_147fc4ea-46d6-4dbd-8882-7b74700e8798-Shrili-72131-72132-scaled.jpg" alt="1970 Cadillac DeVille" />')


def system_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%H:%M:%S")
        return HttpResponse(f"Текущее время: {current_time}")
