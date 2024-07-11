import os
import sys

# Adicione o diretório raiz do projeto ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Opcionalmente, defina variáveis de ambiente específicas para testes
os.environ['FLASK_ENV'] = 'testing'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

# Importar app e db se necessário para inicializar algo no módulo de teste
from app import app, db

# Qualquer outra configuração de inicialização de teste pode ser adicionada aqui
