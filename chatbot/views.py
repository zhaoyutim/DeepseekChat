from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from langchain_openai import ChatOpenAI
from .apps import ChatbotConfig
import yaml
model = None

with open("credentials.yaml") as stream:
    try:
        credential_file = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

class ChatbotTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bot.html'

    def get(self, request):
        return Response({})

class ChatbotGenerateAnswerView(APIView):

    def _draft_response(self, message):
        llm = ChatOpenAI(
            model='deepseek-chat',
            openai_api_key=credential_file.get('deepseekapi'),
            openai_api_base='https://api.deepseek.com',
            max_tokens=1024
        )

        response = llm.invoke(message, temperature=1)

        return response.content

    def get(self, request):
        return Response({'response': 'Dummy Response'})

    def post(self, request):
        # Get the user's message from the request data
        message = request.data['message']

        # Call your deep learning model to generate a response
        response = self._draft_response(message)

        # Return the response as a JSON object
        return Response({'response': response})
