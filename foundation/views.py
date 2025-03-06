from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import PhoneBook

def home(request):
    return HttpResponse('hello world')

def about(request):
    data = { 'message' : 'about page data fetched successfully' }
    return JsonResponse(data)

def contact(request):
    return render(request, "contact.html")

def lists(request):
    items = PhoneBook.objects.all()
    return render(request, "phoneBook.html", {"lists" : items})