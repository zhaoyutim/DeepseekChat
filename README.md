# StableLMChat
Web Chatbot based on DeepSeekV3, Django and Langchain. This WebUI is able to generate ChatGPT like responses with DeepSeekV3 model.

## Repo Structure
    .
    ├── chatbot                                              # Django Apps
    │   ├── views.py                                         # Views contains chat endpoint and frontend template
    ├── DeepSeekChat                                         # Project Folder
    └── README.md

## How to Start the server
Put your credential under the root directory with name credentials.yaml
    
    python manage.py runserver
