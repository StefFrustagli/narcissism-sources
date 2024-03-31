from django.apps import AppConfig


class content_managementConfig(AppConfig):
    """
    AppConfig class for configuring the content_management app.

    This class defines the configuration settings
    for the content_management app,
    including the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): Specifies the default auto field
        for model creation.
        name (str): Specifies the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = "content_management"
