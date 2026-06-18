'''
Popula o banco de dados SQLite com os dados de 'api/data/questions.json'
'''

import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.model.models import Questao, Resposta, Tema, Usuario

# 1. Configuração do Banco de Dados (Mesma do app.py)
basedir = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(basedir, 'api', 'database', 'cybersec_database.db')
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def popular_banco():
    session = SessionLocal()
    try:
        # 2. Carregar os dados do arquivo JSON
        with open('api/data/questions.json', 'r', encoding='utf-8') as f:
            dados_quiz = json.load(f)

        # 3. Criar um Tema padrão (pois Questao tem uma chave estrangeira para Tema)
        nome_tema = "Conscientização em Cibersegurança"
        tema_padrao = session.query(Tema).filter_by(nome=nome_tema).first()
        
        if not tema_padrao:
            tema_padrao = Tema(nome=nome_tema)
            session.add(tema_padrao)
            session.commit() # Salva o tema para gerar o ID dele

        # 4. Inserir as questões e respostas
        questoes_adicionadas = 0
        for item in dados_quiz:
            # Verifica se a questão já existe para evitar duplicatas caso rode o script 2x
            questao_existe = session.query(Questao).filter_by(conteudo=item['texto_pergunta']).first()
            
            if not questao_existe:
                # Cria a nova questão mapeando o JSON para o Modelo
                nova_questao = Questao(
                    conteudo=item['texto_pergunta'],
                    tema_id=tema_padrao.id
                )
                session.add(nova_questao)
                session.flush() # Envia pro banco temporariamente para gerar o nova_questao.id

                # Itera sobre as alternativas daquela questão e cria as Respostas
                for alt in item['alternativas']:
                    nova_resposta = Resposta(
                        texto=alt['texto_alternativa'],
                        e_correta=alt['correta'],
                        questao_id=nova_questao.id
                    )
                    session.add(nova_resposta)
                
                questoes_adicionadas += 1

        #5. insere um usuário e senha
        novo_usuario = Usuario(
            nome="Sampson",
            email="sampson@gmail.com",
            senha="123456"
        )
        session.add(novo_usuario)
        
        # 6. Efetiva todas as mudanças no banco de dados
        session.commit()
        print(f"Sucesso! {questoes_adicionadas} novas questões foram inseridas no banco de dados.")

    except Exception as e:
        session.rollback() # Desfaz as alterações em caso de erro
        print(f"Ocorreu um erro ao popular o banco: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    print("Iniciando a migração de dados do JSON para o SQLite...")
    popular_banco()