from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'runbun'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^cart/$', views.cart, name='cart'),
]
