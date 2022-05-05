from django.apps import AppConfig


class ApexConfig(AppConfig):
    DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
    name = 'apex'

    def ready(self):
        from . import updater
        updater.start()
