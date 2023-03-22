from django.urls import path 

from . import views

app_name = "scrapper"

urlpatterns = [
    path("", views.home, name="home"),
    path("pending/", views.pending, name="pending"),
    path("done/", views.done, name="done"),
    path("details/<int:id>/", views.detail, name="details")
]
