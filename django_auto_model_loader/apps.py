from django.apps import AppConfig

class DjangoAutoModelLoader(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_auto_model_loader'  