from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_all_waterings),
    path("<int:watering_id>", views.get_watering),
]