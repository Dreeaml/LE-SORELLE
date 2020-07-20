from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
import stripe


# Create your views here.
endpoint_secret = settings.ENDPOINT_SECRET

@login_required()
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET
    cart = request.session.get('shopping_cart', {})
    request.session['shopping_cart'] = {}
    if len(cart.items()) > 0:
        line_items = []
        for id, quantity in cart.items():
            product = get_object_or_404(Product, pk=id)
            line_items.append({
                'name' : product.name,
                'amount': int(product.price * 100),
                'currency' : 'sek',
                'quantity' : quantity
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            success_url=request.build_absolute_uri(reverse(checkout_success)),
            cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
        )
        print('shopping_cart')
        print(settings.STRIPE_PUBLISHABLE)  
        return render(request, 'checkout.html',
            {'session_id' : session.id,
            'public_key' : settings.STRIPE_PUBLISHABLE,
        })
    else:
        messages.info(request, "Your cart is empty. Go shopping!")
        request.session['shopping_cart'] = cart
        return redirect(reverse('view_cart'))

@login_required
def checkout_success(request):
    request.session['shopping_cart'] = {}
    return render(request, 'thankyou.html')

@login_required
def checkout_cancelled(request):
    return redirect(reverse('all_products'))
    
@login_required   
@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
        
    if event['type'] == 'checkout.session.completed':
        session =event['data']['object']
        
        handle_checkout_session(session)
    
    return HttpResponse(status=200)

def handle_checkout_session(session):
     print(session)