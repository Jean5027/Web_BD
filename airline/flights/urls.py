from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path("", views.index, name="index.html"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),




]
