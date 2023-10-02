from django.urls import path, include
from . import views

urlpatterns = [
    path("watering/",include("api.v1.watering.urls")),
]
