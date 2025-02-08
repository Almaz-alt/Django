from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def about_me(request):
    if request.method == 'GET':
        return HttpResponse("я алмазбек")


def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse("<h1>я учусь Geeks</h1>"
                            '<img src="https://static-cse.canva.com/blob/847064/29.jpg" />')


def system_time(request):
    if request.method == 'GET':
        my_time = datetime.now()
        return HttpResponse(my_time)
