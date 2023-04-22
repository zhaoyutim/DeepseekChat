from django.apps import AppConfig

from chatbot.initialization import stablelm_initialization


class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
    tokenizer, model = stablelm_initialization()
