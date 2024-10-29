from src.modelo.modelo import Articulo, Comentario
from src.modelo.declarative_base import engine, Base, session

class ArticuloManager:
    def __init__(self, session):
        self.session = session

    def crear_articulo(self, titulo):
        articulo = Articulo(titulo=titulo)
        self.session.add(articulo)
        self.session.commit()
        return articulo

    def leer_articulo(self, articulo_id):
        return self.session.query(Articulo).filter_by(id=articulo_id).first()

    def actualizar_articulo(self, articulo_id, nuevo_titulo):
        articulo = self.leer_articulo(articulo_id)
        if articulo:
            articulo.titulo = nuevo_titulo
            self.session.commit()
        return articulo

    def eliminar_articulo(self, articulo_id):
        articulo = self.leer_articulo(articulo_id)
        if articulo:
            self.session.delete(articulo)
            self.session.commit()
        return articulo

    def agregar_comentario(self, articulo_id, comentario_texto):
        articulo = self.leer_articulo(articulo_id)
        if articulo:
            comentario = Comentario(comentario=comentario_texto, articulo=articulo)
            self.session.add(comentario)
            self.session.commit()
            return comentario
        return None

    def leer_comentarios(self, articulo_id):
        articulo = self.leer_articulo(articulo_id)
        return articulo.comentarios if articulo else None

if __name__ =="__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    articulo = ArticuloManager(session)
    articulo1 = articulo.crear_articulo("Programación Python V3")