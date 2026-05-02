from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone

Base = declarative_base()

# Tabela de Associação (Many-to-Many) entre Questionario e Questao
questionario_questao = Table(
    'questionario_questao',
    Base.metadata,
    Column('questionario_id', Integer, ForeignKey('questionario.id', ondelete="CASCADE"), primary_key=True),
    Column('questao_id', Integer, ForeignKey('questao.id', ondelete="CASCADE"), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)

    questionarios = relationship("Questionario", back_populates="usuario")
    resultados = relationship("Resultado", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(nome='{self.nome}', email='{self.email}')>"


class Tema(Base):
    __tablename__ = 'tema'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)

    questoes = relationship("Questao", back_populates="tema")
    questionarios = relationship("Questionario", back_populates="tema")

    def __repr__(self):
        return f"<Tema(nome='{self.nome}')>"


class Questao(Base):
    __tablename__ = 'questao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    conteudo = Column(Text, nullable=False)
    tema_id = Column(Integer, ForeignKey('tema.id'))

    tema = relationship("Tema", back_populates="questoes")
    
    respostas = relationship("Resposta", back_populates="questao", cascade="all, delete-orphan")    
    questionarios = relationship("Questionario", secondary=questionario_questao, back_populates="questoes")

    def __repr__(self):
        return f"<Questao(conteudo='{self.conteudo[:20]}...')>"


class Questionario(Base):
    __tablename__ = 'questionario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    id_user = Column(Integer, ForeignKey('usuario.id'))
    tema_id = Column(Integer, ForeignKey('tema.id'))

    usuario = relationship("Usuario", back_populates="questionarios")
    tema = relationship("Tema", back_populates="questionarios")
    questoes = relationship("Questao", secondary=questionario_questao, back_populates="questionarios")
    resultados = relationship("Resultado", back_populates="questionario")

    def __repr__(self):
        return f"<Questionario(nome='{self.nome}')>"


class Resposta(Base):
    __tablename__ = 'resposta'

    id = Column(Integer, primary_key=True, autoincrement=True)
    texto = Column(String(255), nullable=False)
    e_correta = Column(Boolean, default=False)
    questao_id = Column(Integer, ForeignKey('questao.id', ondelete="CASCADE"))

    questao = relationship("Questao", back_populates="respostas")

    def __repr__(self):
        return f"<Resposta(texto='{self.texto}', correta={self.e_correta})>"


class Resultado(Base):
    __tablename__ = 'resultado'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota = Column(Float)
    data = Column(DateTime, default=datetime.now(timezone.utc))
    id_user = Column(Integer, ForeignKey('usuario.id'))
    id_questionario = Column(Integer, ForeignKey('questionario.id'))

    usuario = relationship("Usuario", back_populates="resultados")
    questionario = relationship("Questionario", back_populates="resultados")

    def __repr__(self):
        return f"<Resultado(nota={self.nota}, data='{self.data}')>"