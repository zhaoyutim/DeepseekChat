from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .apps import ChatbotConfig
from transformers import StoppingCriteria, StoppingCriteriaList
import torch

model = None

class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        stop_ids = [50278, 50279, 50277, 1, 0]
        for stop_id in stop_ids:
            if input_ids[0][-1] == stop_id:
                return True
        return False

class ChatbotView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bot.html'

    def _draft_response(self, message):
        system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
        - StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
        - StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
        - StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
        - StableLM will refuse to participate in anything that could harm a human.
        """
        user_prompt = message
        prompt = f"{system_prompt}<|USER|>{user_prompt}<|ASSISTANT|>"

        max_new_tokens = 132
        temperature = 0.7
        top_k = 0
        top_p = 0.9
        do_sample = True
        model = ChatbotConfig.model
        tokenizer = ChatbotConfig.tokenizer

        inputs = tokenizer(prompt, return_tensors="pt")
        inputs.to(model.device)

        # Generate
        tokens = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            do_sample=do_sample,
            pad_token_id=tokenizer.eos_token_id,
            stopping_criteria=StoppingCriteriaList([StopOnTokens()])
        )
        completion_tokens = tokens[0][inputs['input_ids'].size(1):]
        response = tokenizer.decode(completion_tokens, skip_special_tokens=True)
        return response

    def get(self, request):
        return Response({'response': 'Dummy Response'})

    def post(self, request):
        # Get the user's message from the request data
        message = request.data['message']

        # Call your deep learning model to generate a response
        response = self._draft_response(message)

        # Return the response as a JSON object
        return Response({'response': response})
