from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.watering),
    path("<int:watering_id>", views.watering_by_id),
]