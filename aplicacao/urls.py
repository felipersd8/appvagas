from django.contrib import admin
from django.urls import path, include
from .views import home  # Importando a função da home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", home, name="home"),  # Adicionando a rota para a home
]
