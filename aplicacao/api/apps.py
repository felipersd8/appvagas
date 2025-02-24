from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'  # ✅ Certifique-se de que está apenas 'api' e não 'aplicacao.api'
