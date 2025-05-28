# config.py

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Config
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-default-secret-key')  # fallback default

    # Mail Config (for password reset, etc.)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    # Other configs
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')