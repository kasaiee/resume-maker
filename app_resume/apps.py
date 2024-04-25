from django.apps import AppConfig
from app_resume.setup_permissions import setup_advanced_user_permissions


class AppResumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_resume'

    def ready(self):
        import app_resume.signals
        setup_advanced_user_permissions()