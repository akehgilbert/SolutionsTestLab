from django.urls import path
from .views import home_view, about_view, services_view, careers_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),           # root page
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('careers/', careers_view, name='careers'),
    path('contact/', contact_view, name='contact'),
]
