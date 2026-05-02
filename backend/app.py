from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.model.init import DATABASE_URL
# Importe dos modelos para consulta
import api.model.models as m

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)