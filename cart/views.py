from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib import messages


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart.html', {'shopping_cart':cart})
    
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    if quantity > 0:
        cart = request.session.get('shopping_cart', {})
        if id in cart:
            cart[id] = int(cart[id]) + quantity 
        else:
            cart[id] = cart.get(id, quantity) 

        messages.success(request, "Your cart has been updated!")
        request.session['shopping_cart'] = cart
        return redirect(reverse('all_products'))
    else:
        messages.success(request, "Please add at least 1 product!")

def decrease_product_quantity(request, id):
    cart = request.session.get('shopping_cart', {})
    if id in cart:
        if int(cart[id]) > 1:
            cart[id] = int(cart[id]) - 1
        else:
            del cart[id]
    request.session['shopping_cart'] = cart #update current session cart to this cart instance
    return redirect(reverse('view_cart'))

def increase_product_quantity(request, id):
    cart = request.session.get('shopping_cart', {})
    if id in cart:
        if int(cart[id]) > 0:
            cart[id] = int(cart[id]) + 1 #if exists, add ID & quantity
    request.session['shopping_cart'] = cart #update current session cart to this cart instance
    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    cart=request.session.get('shopping_cart', {})
    
    # Remove the products specified by the products_id argument to cart
    if id in cart:
        del cart[id]
    
    request.session['shopping_cart'] = cart
    return redirect('view_cart')


def back_to_shop(request, id):
    """return to products.html to keep shopping"""
    return redirect(reverse('all_products'))

    