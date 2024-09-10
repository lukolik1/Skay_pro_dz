from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductList(ListView):
    model = Product





def contacts(request):
    return render(request, 'contacts.html')


class ProductDetail(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCrearte(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    exclude = ['created_at', 'updated_at']
    success_url = reverse_lazy('catalog:product_lsit')
    
class ProductUpdate(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    exclude = ['created_at', 'updated_at']
    success_url = reverse_lazy('catalog:product_lsit')

    def get_success_url(self):
        return reversed('catalog:products_detail', args=(self.kwargs.get('pk')))


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_lsit')
