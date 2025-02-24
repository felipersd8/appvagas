from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet, VagaViewSet, profissionais_destaque

router = DefaultRouter()
router.register(r'profissionais', ProfissionalViewSet)
router.register(r'vagas', VagaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profissionais/destaque/', profissionais_destaque, name='profissionais-destaque'),  # Adicionando o endpoint corretamente
]
