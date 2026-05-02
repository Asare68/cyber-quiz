#!/bin/bash

# Inicia o backend
cd backend
# source venv/Scripts/activate # Inicialização para Windows
source .venv/bin/activate # Inicialização para Linux
pip install flask flask_cors sqlalchemy
python app.py &

# Inicia o frontend
cd ../frontend
npx expo start