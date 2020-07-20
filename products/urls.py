from django.conf.urls import url
from .views import home_products, all_products, product_detail, coming_soon, faq

urlpatterns = [
    url(r'^$', home_products,  name="products"),
    url(r'^all_products/$', all_products,  name="all_products"),
    url(r'^(\d+)$', product_detail, name='product_detail'),
    url(r'^(?P<category>[\w-]+)/$', all_products, name='all_products'),
    url(r'^coming$', coming_soon, name='coming_soon'),
    url(r'^faq$', faq, name='faq'),
]