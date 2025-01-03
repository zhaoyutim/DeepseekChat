# StableLMChat
Web Chatbot based on DeepSeekV3, Django and Langchain. This WebUI is able to generate ChatGPT like responses with DeepSeekV3 model.

## Repo Structure
    .
    ├── chatbot                                              # Django Apps
    │   ├── views.py                                         # Views contains chat endpoint and frontend template
    │   ├── initialization.py                                # Initialization StableLM model in Local machine
    ├── StableLMChat                                         # Project Folder
    └── README.md

## How to Start the server

    python manage.py runserver --noreload (--noreload is to make sure model is loaded only once during development)
