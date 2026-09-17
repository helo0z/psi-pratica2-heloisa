from consultas import (
    buscar_livros_por_titulo,
    exibir_detalhes_livro,
    listar_autores_quantidade_livros,
    listar_livros_por_autor,
    listar_todos_livros_com_autor,
)
from database import criar_banco
from seed import popular_banco


def main():
    criar_banco()
    popular_banco()

    listar_todos_livros_com_autor()
    listar_livros_por_autor("Machado de Assis")
    buscar_livros_por_titulo("Memórias")
    listar_autores_quantidade_livros()
    exibir_detalhes_livro(1)


if __name__ == "__main__":
    main()