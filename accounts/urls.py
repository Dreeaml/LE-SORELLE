from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^registration/$', registration, name="registration"),
    url(r'^user_profile/$', user_profile, name="user_profile"),
    url(r'^password-reset/', include(urls_reset)),

]