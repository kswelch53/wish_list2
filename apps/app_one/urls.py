#app-level url code:
from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'register$', views.register, name = "register"),
    url(r'login$', views.login, name="login"),
    url(r'logout$', views.logout, name="logout"),
]
#index is the named route for the root route to index function in views.py
#register is the named route for the form action register to the register function in views.py
