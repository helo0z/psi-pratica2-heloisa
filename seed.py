from database import nova_sessao
from models import Autor, Livro


def popular_banco():
    with nova_sessao() as session:
        if session.query(Autor).first():
            return

        autor1 = Autor(nome="Machado de Assis", pais="Brasil")
        autor2 = Autor(nome="George Orwell", pais="Reino Unido")
        autor3 = Autor(nome="Clarice Lispector", pais="Brasil")

        livro1 = Livro(titulo="Dom Casmurro", ano=1899, autor=autor1)
        livro2 = Livro(
            titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=autor1
        )
        livro3 = Livro(titulo="Quincas Borba", ano=1891, autor=autor1)
        livro4 = Livro(titulo="1984", ano=1949, autor=autor2)
        livro5 = Livro(titulo="A Revolução dos Bichos", ano=1945, autor=autor2)
        livro6 = Livro(titulo="A Hora da Estrela", ano=1977, autor=autor3)

        session.add_all([autor1, autor2, autor3])
        session.add_all([livro1, livro2, livro3, livro4, livro5, livro6])

        session.commit()