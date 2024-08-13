from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    context = {'products': Product.objects.all()}
    return render(request, 'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')


def products_detail(request, pk):
    context = {'product': get_object_or_404(Product, pk=pk)}
    return render(request, 'products_detail.html', context)





