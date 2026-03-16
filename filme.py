from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Criar a classe base do orm
Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    genero = Column(String(100), nullable=False)
    ano_lancamento = Column(Integer, nullable=False)
    nota = Column(Float)
    disponivel = Column(Boolean, default=True)

    def __init__(self, titulo, genero, ano_lancamento, nota, disponivel=True):
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.nota = nota
        self.disponivel = disponivel
    
    def __repr__(self):
        return f"<Filme titulo='{self.titulo}', genero='{self.genero}', ano={self.ano_lancamento}>"

# Criar Conexão com o banco de dados
engine = create_engine("sqlite:///catalogo_filmes.db")

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

