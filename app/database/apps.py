from django.apps import AppConfig


class DatabaseConfig(AppConfig):
    name = 'database'
    verbose_name = 'Baza danych'


    def ready(self):
        import database.signals