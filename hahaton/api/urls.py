from django.urls import path

from api import views

urlpatterns = [
        path('', views.index, name="index"),
        path('search_page', views.search_page, name="search_page"),
]
