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

#Função para adicionar um filme
def cadastrar_filme():
    print("=== Cadastro de Filme ===")
    titulo = input("Título: ")
    genero = input("Gênero: ")
    ano = int(input("Ano de Lançamento: "))
    nota = float(input("Nota: "))

    with Session() as carrinho:
        try:
            filme_existente = carrinho.query(Filme).filter_by(titulo=titulo,ano_lancamento=ano).first()
            if filme_existente == None:
                novo_filme = Filme(titulo, genero, ano, nota)
                carrinho.add(novo_filme)
                carrinho.commit()
                print("Filme cadastrado com sucesso!")
            else:
                print("Já existe um filme com esse título e ano de lançamento.")
        except Exception as erro:
            carrinho.rollback()
            print(f"Ocorreu um erro: {erro}")

# Criar a função para listar os filmes, atualizar e excluir
def listar_filmes():
    try:
        print("=== filmes cadastrados ===")
        with Session() as carrinho:
            filmes = carrinho.query(Filme).all()
            for filme in filmes:
                print(f"Título: {filme.titulo}, Gênero: {filme.genero}, Ano: {filme.ano_lancamento}, Disponível: {filme.disponivel}")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")

def atualizar_filme():
    print("=== Atualizar Filme ===")
    titulo = input("Digite o título do filme que deseja atualizar: ")

    with Session() as carrinho:
        try:
            filme = carrinho.query(Filme).filter_by(titulo=titulo).first()
            if filme:
                novo_titulo = input(f"Novo título (atual: {filme.titulo}): ")
                novo_genero = input(f"Novo gênero (atual: {filme.genero}): ")
                novo_ano = int(input(f"Novo ano de lançamento (atual: {filme.ano_lancamento}): "))
                nova_nota = float(input(f"Nova nota (atual: {filme.nota}): "))
                filme.titulo = novo_titulo
                filme.genero = novo_genero
                filme.ano_lancamento = novo_ano
                filme.nota = nova_nota
                carrinho.commit()
                print("Filme atualizado com sucesso!")
            else:
                print("Filme não encontrado.")
        except Exception as erro:
            carrinho.rollback()
            print(f"Ocorreu um erro: {erro}")

def excluir_filme():
    print("=== Excluir Filme ===")
    titulo = input("Digite o título do filme que deseja excluir: ")

    with Session() as carrinho:
        try:
            filme = carrinho.query(Filme).filter_by(titulo=titulo).first()
            if filme:
                carrinho.delete(filme)
                carrinho.commit()
                print("Filme excluído com sucesso!")
            else:
                print("Filme não encontrado.")
        except Exception as erro:
            carrinho.rollback()
            print(f"Ocorreu um erro: {erro}")