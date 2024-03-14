from django.apps import AppConfig


class AppResumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_resume'

    def ready(self):
        import app_resume.signals
