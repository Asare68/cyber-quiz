from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import jwt
import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.model.init import DATABASE_URL
# Importe dos modelos para consulta
import api.model.models as m

app = Flask(__name__)
CORS(app)


#BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load questions
#with open('data/questions.json', 'r', encoding='utf-8') as f:
    #quiz_data = json.load(f)

#with open(os.path.join(BASE_DIR, 'api', 'data', 'questions.json'), 'r', encoding='utf-8') as f:
#    quiz_data = json.load(f)

# Configuração do banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#this is the insecure way of doing this because you can not have the secret key in the code
#fix it later .
SECRET_KEY = "sua_chave_secreta_muito_forte_12345"

#@app.route('/api/quiz', methods=['GET'])
#def get_quiz():
#    return jsonify(quiz_data)

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    session = SessionLocal()

    try:
        questoes = session.query(m.Questao).all()
        temas = session.query(m.Tema).all()
        
        quiz_data = []
        for questao in questoes:
            quiz_data.append({
                "id": questao.id,
                "conteudo": questao.conteudo,
                "tema_id": questao.tema_id,
                "respostas": [
                    {
                        "id": resp.id,
                        "texto": resp.texto,
                        "e_correta": resp.e_correta
                    } for resp in questao.respostas
                ],
            })
        for tema in temas:
            quiz_data.append({
                "id_tema": tema.id,
                "nome_tema": tema.nome
            })
        
        return jsonify(quiz_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

@app.route('/api/login', methods=['POST'])
def login():
    Session = SessionLocal()

    try:
      #i have to change this to get the data from the resquest  
        data = request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"error": "Missing email or password"}), 400

        email = data['email']
        password = data['password']
        token = jwt.encode({
            'email': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm='HS256')

        usuario = (Session.query(m.Usuario).filter_by(email=email, senha=password).first())

        if (usuario is None):
            return jsonify({"error": "Invalid email or password"}), 401
        
        return jsonify({
            "message": "Login successful",
            "email": email,
            "token": token,
            "status": "success"
        }), 200
    except Exception:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)