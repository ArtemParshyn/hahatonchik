from django.urls import path

from api import views

urlpatterns = [
        path('', views.index, name="index"),
        path('services', views.services, name="index"),
        path('about', views.about, name="index"),
        path('contact', views.contact, name="index"),
]
