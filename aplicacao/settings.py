import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# 🔹 Carrega variáveis de ambiente do arquivo .env (se estiver rodando localmente)
load_dotenv()

# 📌 Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔒 Mantenha essa chave segura e use um .env para esconder em produção!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-fallback-key")

# ⚠️ Em produção, altere para False e configure ALLOWED_HOSTS corretamente!
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# 🖥️ Defina os hosts permitidos (em produção, adicione domínios reais)
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

# 🛠️ Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicações do projeto
    'aplicacao.api',

    # Django REST Framework e autenticação
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',

    # Documentação da API
    'drf_yasg',

    # Segurança e controle de CORS
    'corsheaders',
]

# 🚀 Middleware (incluindo CORS)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "aplicacao.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "aplicacao" / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "aplicacao.wsgi.application"

# 📂 Banco de Dados (Configuração automática para PostgreSQL ou SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "django_db"),
        'USER': os.getenv("POSTGRES_USER", "django_user"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "senha_forte"),
        'HOST': os.getenv("POSTGRES_HOST", "db"),  # Mantém "db" para containers
        'PORT': os.getenv("POSTGRES_PORT", "5432"),
    }
}

# 🔑 Validação de Senhas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# 🎨 Configuração de arquivos estáticos e mídia
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "aplicacao" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# 📜 Configuração de Paginação e Autenticação JWT no Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Exige autenticação para acessar APIs
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# 🔒 Configuração do JWT para controle de expiração do token
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Token válido por 30 minutos
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # Refresh Token dura 7 dias
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# 🌐 Permissão de CORS (para consumir API de um frontend)
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", "True") == "True"

# 🔐 Definição de domínios confiáveis para requisições CSRF (caso use um frontend separado)
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "http://127.0.0.1:8000,http://localhost:8000").split(",")

# 🔑 Chave Padrão para Modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
