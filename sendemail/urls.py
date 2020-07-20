from django.conf.urls import url
from .views import contact_us, successView

urlpatterns = [
    url(r'^$', contact_us, name="contact_us"),
    url(r'^email_success/$', successView, name="email_success"),
]