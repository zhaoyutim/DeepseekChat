from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.conf import settings
model = None

class ChatbotView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chatbot.html'

    def _draft_response(self, message):
        response='Dummy response'
        return response

    def get(self, request):
        return Response()

    def post(self, request):
        # Get the user's message from the request data
        message = request.data['message']

        # Call your deep learning model to generate a response
        response = self._draft_response(message)

        # Return the response as a JSON object
        return Response({'response': response})
