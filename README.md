# Projeto: Aula - ORM com SQLAlchemy

Resumo rápido
- Este repositório demonstra o uso básico do SQLAlchemy com SQLite para modelagem de dados e operações CRUD.
- Arquivos principais: [main.py](main.py) e [filme.py](filme.py).

Arquivos no workspace
- [main.py](main.py) — define o modelo [`Usuario`](main.py) e cria/insere um usuário em `empresa.db`.
- [filme.py](filme.py) — define o modelo [`Filme`](filme.py) e fornece as funções interativas: [`cadastrar_filme`](filme.py), [`listar_filmes`](filme.py), [`atualizar_filme`](filme.py) e [`excluir_filme`](filme.py).
- [catalogo_filmes.db](catalogo_filmes.db) — banco SQLite usado por [filme.py](filme.py).
- [empresa.db](empresa.db) — banco SQLite usado por [main.py](main.py).
- [.gitignore](.gitignore) — regras de ignore do Git para o projeto.
- [README.md](README.md) — este arquivo.

*Utilizar o .venv é opcional*

Como configurar e executar
1. Criar ambiente virtual (recomendado):
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix/macOS
source .venv/bin/activate
```

2. Instalar dependência:
```bash
pip install SQLAlchemy
```

3. Executar o exemplo de criação de usuário:
```bash
python main.py
```
- O script [main.py](main.py) cria o banco `empresa.db`, a tabela (via [`Base`](main.py).metadata.create_all) e tenta inserir um usuário usando a sessão [`Session`](main.py).

4. Testar operações de filmes (interativo):
- Importar e chamar funções do arquivo [filme.py](filme.py):
```bash
python -c "import filme; filme.cadastrar_filme()"
```
ou abrir REPL:
```bash
python -i filme.py
# então chame: cadastrar_filme(), listar_filmes(), atualizar_filme(), excluir_filme()
```

Explicação de como cada parte foi feita

- Modelos e base do ORM
  - A classe [`Usuario`](main.py) e a classe [`Filme`](filme.py) herdam de [`Base`](main.py) / [`Base`](filme.py) (ambas criadas com `declarative_base()`), que fornece o mapeamento declarativo do SQLAlchemy.
  - Colunas são definidas com `Column(...)` e tipos (`Integer`, `String`, `Float`, `Boolean`). Ex.: `id = Column(Integer, primary_key=True, autoincrement=True)`.

- Conexão e engine
  - Cada módulo cria um `engine` apontando para um arquivo SQLite:
    - Em [main.py](main.py): `engine = create_engine("sqlite:///empresa.db")` — cria/usa `empresa.db`.
    - Em [filme.py](filme.py): `engine = create_engine("sqlite:///catalogo_filmes.db")` — cria/usa `catalogo_filmes.db`.

- Criação de tabelas
  - Chamadas a `Base.metadata.create_all(engine)` (em cada arquivo) criam as tabelas definidas pelos modelos caso não existam.

- Sessões e transações
  - `Session = sessionmaker(bind=engine)` cria a fábrica de sessões.
  - Blocos `with Session() as session:` são usados para abrir uma sessão que fecha automaticamente.
  - `session.commit()` persiste mudanças; em caso de erro, `session.rollback()` desfaz a transação.

- Operações CRUD em [filme.py](filme.py)
  - [`cadastrar_filme`](filme.py): solicita dados via `input()`, checa duplicata (`filter_by(titulo=..., ano_lancamento=...)`) e insere novo registro.
  - [`listar_filmes`](filme.py): busca todos os filmes com `query(Filme).all()` e exibe.
  - [`atualizar_filme`](filme.py): localiza por título, atualiza atributos e faz `commit()`.
  - [`excluir_filme`](filme.py): localiza por título, usa `session.delete()` e faz `commit()`.

Boas práticas e observações
- Emails em [`Usuario`](main.py) configurados com `unique=True` para evitar duplicatas.
- As funções em [filme.py](filme.py) são interativas (usam `input()`); para teste automatizado, converter para funções que recebem parâmetros.
- Adicionar um `requirements.txt` pode facilitar instalações futuras:
```text
SQLAlchemy
```

Referências rápidas (símbolos e arquivos)
- Modelo: [`Usuario`](main.py)
- Sessão/engine: [`engine`](main.py), [`Session`](main.py)
- Modelo e funções de filme: [`Filme`](filme.py), [`cadastrar_filme`](filme.py), [`listar_filmes`](filme.py), [`atualizar_filme`](filme.py), [`excluir_filme`](filme.py)
- Arquivos: [main.py](main.py), [filme.py](filme.py), [catalogo_filmes.db](catalogo_filmes.db)

Feito por Kaylan teodoro.