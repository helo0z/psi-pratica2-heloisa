from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    pais: Mapped[str] = mapped_column(String(50), nullable=False)

    livros: Mapped[List["Livro"]] = relationship(
        back_populates="autor", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Autor(id={self.id}, nome='{self.nome}', pais='{self.pais}')>"


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)

    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"), nullable=False)

    autor: Mapped["Autor"] = relationship(back_populates="livros")

    def __repr__(self) -> str:
        return f"<Livro(id={self.id}, titulo='{self.titulo}', ano={self.ano})>"