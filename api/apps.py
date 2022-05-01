from django.apps import AppConfig



class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from api.models import Profile  
        from django.urls import register_converter
        from api.models.common import PathModelConverter

        register_converter(PathModelConverter(Profile), 'profile')  # Simple usage, by integer ID
    #     # register_converter(PathModelConverter(Account, field='username', regex='[a-zA-Z0-9._-]+'), 'username')  # Complex usage, with custom field and regex


