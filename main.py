from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

#Criar a classe base do orm
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    #Coluna de ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nullable=False -> campo obrigatório
    nome = Column(String(100), nullable=False)
    # unique=True -> campo único, não pode haver dois usuários com o mesmo email
    email = Column(String(100), nullable=False, unique=True)

    idade = Column(Integer)

    ativo = Column(Boolean, default=True)

    salario = Column(Float)

    def __init__(self, nome, email, idade, salario):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.salario = salario

# Criar Conexão com o banco de dados
# PostgreSQL: "postgresql://usuario:senha@localhost/nomedobanco"
# MySQL: "mysql+pymysql://usuario:senha@localhost/nomedobanco"
engine = create_engine("sqlite:///empresa.db")

#Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

with Session() as session:
    try:
        #Antes de inserir, buscamos um usuário com esse email
        usuario_existente = session.query(Usuario).filter_by(email="kaylan@gmail.com").first()

        if usuario_existente == None:
            #Criamos um obejto da classe Usuario
            usuario = Usuario("Kaylan", "kaylan@gmail.com", 30, 5000)
            session.add(usuario)
            session.commit()
            print("Usuário criado com sucesso!")
        else:
            print("Já existe um usuário com esse email.")

    except Exception as erro:
        # se ocorrer qualquer erro durante o commit
        # desfaça a transição atual
        session.rollback()
        print(f"Ocorreu um erro: {erro}")