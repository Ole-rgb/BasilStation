from django.urls import path, include
from . import views

urlpatterns = [
    path("v1/",include("api.v1.urls")),
]
