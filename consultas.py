from sqlalchemy import func, select
from database import nova_sessao
from models import Autor, Livro


def listar_todos_livros_com_autor():
    with nova_sessao() as session:
        stmt = select(Livro)
        livros = session.scalars(stmt).all()
        for livro in livros:
            print(f"Livro: {livro.titulo} | Autor: {livro.autor.nome}")


def listar_livros_por_autor(nome_autor: str):
    with nova_sessao() as session:
        stmt = select(Autor).where(Autor.nome.ilike(f"%{nome_autor}%"))
        autor = session.scalars(stmt).first()
        if autor:
            for livro in autor.livros:
                print(f"- {livro.titulo} ({livro.ano})")


def buscar_livros_por_titulo(termo: str):
    with nova_sessao() as session:
        stmt = select(Livro).where(Livro.titulo.ilike(f"%{termo}%"))
        livros = session.scalars(stmt).all()
        for livro in livros:
            print(f"- {livro.titulo} (Autor: {livro.autor.nome})")


def listar_autores_quantidade_livros():
    with nova_sessao() as session:
        stmt = (
            select(Autor.nome, func.count(Livro.id))
            .outerjoin(Autor.livros)
            .group_by(Autor.id)
        )
        resultados = session.execute(stmt).all()
        for nome, total in resultados:
            print(f"Autor: {nome} | Quantidade de livros: {total}")


def exibir_detalhes_livro(id_livro: int):
    with nova_sessao() as session:
        stmt = select(Livro).where(Livro.id == id_livro)
        livro = session.scalars(stmt).first()
        if livro:
            print(f"Título: {livro.titulo}")
            print(f"Ano de Lançamento: {livro.ano}")
            print(f"Autor: {livro.autor.nome}")
            print(f"País do Autor: {livro.autor.pais}")