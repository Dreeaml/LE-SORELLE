from django.conf.urls import url
from .views import index, faq, sizes

urlpatterns = [
    url(r'^$', index, name='index'),
    url('^faq/$', faq, name='faq'),
    url('^sizes/$', sizes, name='sizes'),
]
