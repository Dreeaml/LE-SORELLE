from django.conf.urls import url
from .views import checkout, checkout_success, checkout_cancelled, payment_completed

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^success/$', checkout_success,  name="checkout_success"),
    url(r'^cancelled/$', checkout_cancelled,  name="checkout_cancelled"),
    url(r'^payment_completed/$', payment_completed)
]
