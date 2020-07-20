from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.
def search(request):
    """
       A view that displays all bugs and features that match the users
       search term(s)
     """
    products = Product.objects.filter(
        Q(name__icontains=request.GET['search']))


    return render(request, "search.html", {"products": products})
