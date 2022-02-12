from django.apps import AppConfig


class StreamersConfig(AppConfig):
    name = 'streamers'

    def ready(self):
        import streamers.signals 
        
