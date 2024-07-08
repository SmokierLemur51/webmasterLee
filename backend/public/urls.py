from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='public-index'),
    path('about', views.about, name='public-about'),
    path('contact', views.contact, name='public-contact'),
]