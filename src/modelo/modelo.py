from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from src.modelo.declarative_base import Base

class Articulo(Base):
    __tablename__ = 'articulos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    comentarios = relationship("Comentario", back_populates="articulo", cascade="all, delete-orphan")


class Comentario(Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    comentario = Column(String, nullable=False)
    articulo_id = Column(Integer, ForeignKey('articulos.id'))
    articulo = relationship("Articulo", back_populates="comentarios")



