from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Profissional, Vaga
from .serializers import ProfissionalSerializer, VagaSerializer
from .permissions import IsAdminOrReadOnly  # Certifique-se de que esse import está correto

# ✅ Criando a view para profissionais em destaque
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profissionais_destaque(request):
    """
    Retorna uma lista de profissionais que possuem destaque no sistema.
    """
    profissionais = Profissional.objects.filter(destaque=True).order_by("id")  # Ordenação corrigida
    serializer = ProfissionalSerializer(profissionais, many=True)
    return Response(serializer.data)

# ✅ ViewSet para Profissional com ordenação corrigida
class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all().order_by("id")  # Adicionando ordenação por ID
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nome', 'profissao', 'email']
    search_fields = ['nome', 'profissao', 'email']
    ordering_fields = ['nome', 'profissao']

# ✅ ViewSet para Vaga com ordenação corrigida
class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all().order_by("id")  # Adicionando ordenação por ID
    serializer_class = VagaSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['titulo', 'descricao', 'salario']
    search_fields = ['titulo', 'descricao']
    ordering_fields = ['titulo', 'salario']
