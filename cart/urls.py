from django.conf.urls import url
from .views import view_cart, add_to_cart, remove_from_cart, decrease_product_quantity, increase_product_quantity

urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    url(r'^add/(?P<id>\d+)$', add_to_cart, name="add_to_cart"),
    #url(r'^add_one/(?P<id>\d+)$', add_one_to_cart, name="add_one_to_cart"),
    url(r'^remove/(?P<id>\d+)$', remove_from_cart, name="remove_from_cart"),
    url(r'^increase/(?P<id>\d+)$', increase_product_quantity, name="increase_product_quantity"),
    url(r'^decrease/(?P<id>\d+)$', decrease_product_quantity, name="decrease_product_quantity"),
]