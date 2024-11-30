from django.urls import path

from api import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services/', views.services, name="services"),
    path('all-employees/', views.all_employees, name="all_employees"),
    path('about/', views.about, name="about"),
    path('', views.index, name="index"),
    path('search_page', views.search_page, name="search_page"),
]
