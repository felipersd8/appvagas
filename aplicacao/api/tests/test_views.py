import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from api.models import Profissional, Vaga

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    user = User.objects.create_user(username="testuser", password="testpass")
    return user

@pytest.fixture
def create_profissional(db):
    return Profissional.objects.create(nome="João Silva", profissao="Engenheiro", email="joao@email.com")

@pytest.fixture
def create_vaga(db):
    return Vaga.objects.create(titulo="Vaga de Engenheiro", descricao="Descrição da vaga", salario=5000)

def test_login(api_client, create_user):
    response = api_client.post("/api/token/", {"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access" in response.data  # Verifica se o token foi gerado corretamente

def test_get_profissionais(api_client, create_user, create_profissional):
    # Autenticar o usuário antes da requisição
    api_client.force_authenticate(user=create_user)

    response = api_client.get("/api/profissionais/")
    assert response.status_code == 200

def test_get_vagas(api_client, create_user, create_vaga):
    # Autenticar o usuário antes da requisição
    api_client.force_authenticate(user=create_user)

    response = api_client.get("/api/vagas/")
    assert response.status_code == 200

def test_create_profissional_unauthorized(api_client):
    response = api_client.post("/api/profissionais/", {"nome": "Teste", "profissao": "Dev", "email": "teste@email.com"})
    assert response.status_code == 401  # Certifica que usuários não autenticados não podem criar

def test_create_vaga_unauthorized(api_client):
    response = api_client.post("/api/vagas/", {"titulo": "Nova Vaga", "descricao": "Teste", "salario": 4000})
    assert response.status_code == 401  # Certifica que usuários não autenticados não podem criar
