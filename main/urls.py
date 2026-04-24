from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('membership/', views.membership, name='membership'),
    path('contact/', views.contact, name='contact'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
]
