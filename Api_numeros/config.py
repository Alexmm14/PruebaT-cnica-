import os

# Clase config para hacer la conexión con la BD
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    POSTGRES_USER = os.environ.get('DB_USER')
    POSTGRES_PASSWORD = os.environ.get('DB_PASSWORD')
    POSTGRES_HOST = os.environ.get('DB_HOST')
    POSTGRES_DB = os.environ.get('DB_NAME') 
    

    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

   