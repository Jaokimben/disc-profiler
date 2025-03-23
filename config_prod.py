# Préparation pour le déploiement

# Configuration pour l'environnement de production
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class ProductionConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cle-secrete-pour-production'
    DEBUG = False
    # Autres configurations de production si nécessaires
