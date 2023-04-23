# StableLMChat
Web Chatbot based on StableLM and Django

## Repo Structure
    .
    ├── chatbot                                              # Django Apps
    │   ├── views.py                                         # Views contains chat endpoint and frontend template
    │   ├── initialization.py                                # Initialization StableLM model in Local machine
    ├── StableLMChat                                         # Project Folder
    └── README.md

## How to Start the server

python manage.py runserver --noreload (--noreload is to make sure model is loaded only once during development)
