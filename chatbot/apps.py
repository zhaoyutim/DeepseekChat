from django.apps import AppConfig

from chatbot.initialization import stablelm_initialization


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
    loaded_weights = False
    if not loaded_weights:
        tokenizer, model = stablelm_initialization()

    def ready(self):
        if ChatbotConfig.loaded_weights: return
        ChatbotConfig.loaded_weights = True
