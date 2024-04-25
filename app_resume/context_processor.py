from django.conf import settings

def get_settings(request):
    return {
        'version': settings.VERSION
    }