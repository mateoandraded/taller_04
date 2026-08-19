from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.ActividadesAPI.as_view(), name="actividades_api_resources"),
]
