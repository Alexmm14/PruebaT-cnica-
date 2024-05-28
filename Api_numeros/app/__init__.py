from flask import Flask
from config import Config
from datetime import datetime, timedelta




def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    
    from app import routes  # Importa tus rutas después de configurar todo

    return app
