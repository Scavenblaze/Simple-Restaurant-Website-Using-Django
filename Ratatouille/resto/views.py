from datetime import datetime

from django.shortcuts import render

from resto.models import Book

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def menu(request):
    return render(request, 'menu.html')

def form(request):
    if request.method == "POST":
        CustomerName = request.POST.get('CustomerName')
        CustomerEmail = request.POST.get('CustomerEmail')
        ContactNumber = request.POST.get('ContactNumber')
        book = Book(CustomerName = CustomerName, CustomerEmail = CustomerEmail, ContactNumber = ContactNumber, Date = datetime.today())
        book.save()
    return render(request, 'form.html')