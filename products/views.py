from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Category, Product, Size, Color, Stock
from django.core.paginator import Paginator
from .forms import ProductsSearch
       
def home_products(request):
    products = Product.objects.all()
    return render(request, "home_products.html", {"products": products })

def all_products(request, category=""):
    search_form  = ProductsSearch()
    products = Product.objects.all()

    # Display all products
    if request.GET.get('search_terms'):
        product1=request.GET.get('search_terms')
        products = products.filter(name__contains=product1.capitalize())
    
    if category != "":
        products = products.filter(category__category__exact=category)
    
    return render(request, "all_products.html",{ 
        "products": products,
        'search_products':search_form,
        })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request,
                  'product_detail.html', {'product': product}) 

def coming_soon(request):
    return render(request, 'coming_soon.html')

def faq(request):
    return render(request, 'faq.html')
