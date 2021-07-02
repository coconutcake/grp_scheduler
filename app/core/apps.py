from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Zarządzanie kontami użytkowników'

    # def ready(self):
    #     import core.signals