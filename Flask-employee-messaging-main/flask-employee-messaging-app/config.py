import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:Budai2001@127.0.0.1:2001/messaging_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
