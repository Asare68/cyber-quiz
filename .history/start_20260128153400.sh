#!/bin/bash

# Inicia o backend
cd backend
source .venv/Scripts/activate
pip install flask flask_cors
python3 app.py &

# Inicia o frontend
cd ../frontend
npx expo start
