from django.shortcuts import get_object_or_404
from products.models import Product

"""Displays the Cart context which is available to all webpages/apps"""
def cart_contents(request):
    
    #Request existing cart if it exists or blank cart if not
    cart = request.session.get("shopping_cart", {})

    #Initialize cart items
    cart_items = []
    subtotal = 0
    total = 0
    product_count = 0

    #For loop takes record ID and quantity in cart
    for id, quantity in cart.items():
        #get record object using primary key
        product = get_object_or_404(Product, pk=id)
        
        #Calculate total by adding multiplication of quantity with price
        subtotal = product.price * quantity


        #Calculate total by adding multiplication of quantity with price
        total += quantity * product.price
        
        #increment count as quantity increases
        product_count += quantity
        
        #Append each item  to the cart array/list
        cart_items.append({'id': id, 'quantity': quantity,'subtotal':subtotal, 'product': product})
    
    #Return a dictionary of key/value pairs
    return {'cart_items': cart_items, 'total': total,'subtotal':subtotal, 'product_count': product_count}