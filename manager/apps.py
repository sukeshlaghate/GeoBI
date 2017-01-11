from django.apps import AppConfig


class ManagerConfig(AppConfig):
    name = 'manager'

    # startup code goes in here. Code is called once when django starts up
    def ready(self):
        pass