from django.apps import AppConfig
from django.core.signals import request_finished
from django.dispatch import receiver


class WwwConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'www'

    def ready(self):
        from .scheduler import scheduler
        if not scheduler.running:
            scheduler.start()


@receiver(request_finished)
def on_request_finished(sender, **kwargs):
    from .scheduler import stop_scheduler
    stop_scheduler()
