from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # Do this to reduce side effect of import on top
        import users.signal
    