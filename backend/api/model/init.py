from sqlalchemy import create_engine
from api.model.models import Base # PARA RODAR DE ROOT (backend): python -m api.model.init

# Cria o arquivo SQLite no diretório atual
DATABASE_URL = "sqlite:///api/database/cybersec_database.db"

# Cria o "motor" do banco de dados 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria todas as tabelas definidas no Base
Base.metadata.create_all(bind=engine)

print("Banco de dados SQLite criado com sucesso!")