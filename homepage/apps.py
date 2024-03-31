from django.apps import AppConfig


class HomepageConfig(AppConfig):
    """
    Configuration class for the 'homepage' Django app.

    This class defines configuration settings for the 'homepage' app,
    including the default auto field and the app name.

    Attributes:
        default_auto_field (str): Specifies the name of the default auto field
            to use for models in the app.
        name (str): Specifies the name of the app ('homepage').
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'
