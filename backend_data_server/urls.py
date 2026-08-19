from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("actividades/api/", include("actividades_api.urls")),
]
