import unittest
from src.modelo.declarative_base import Session, Base, engine
from src.logica.ArticuloManager import ArticuloManager


class TestArticuloManager(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        # Configurar una nueva sesión para cada prueba
        self.session = Session()
        self.manager = ArticuloManager(self.session)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_crear_articulo(self):
        articulo = self.manager.crear_articulo("Primer Articulo")
        self.assertIsNotNone(articulo.id)
        self.assertEqual(articulo.titulo, "Primer Articulo")

    def test_leer_articulo(self):
        articulo = self.manager.crear_articulo("Articulo para Leer")
        articulo_leido = self.manager.leer_articulo(articulo.id)
        self.assertEqual(articulo_leido.titulo, "Articulo para Leer")

    def test_actualizar_articulo(self):
        articulo = self.manager.crear_articulo("Articulo Original")
        actualizado = self.manager.actualizar_articulo(articulo.id, "Articulo Actualizado")
        self.assertEqual(actualizado.titulo, "Articulo Actualizado")

    def test_eliminar_articulo(self):
        articulo = self.manager.crear_articulo("Articulo a Eliminar")
        eliminado = self.manager.eliminar_articulo(articulo.id)
        self.assertIsNone(self.manager.leer_articulo(eliminado.id))

    def test_agregar_comentario(self):
        articulo = self.manager.crear_articulo("Articulo con Comentario")
        comentario = self.manager.agregar_comentario(articulo.id, "Este es un comentario")
        self.assertEqual(comentario.comentario, "Este es un comentario")
        self.assertEqual(comentario.articulo_id, articulo.id)

    def test_leer_comentarios(self):
        articulo = self.manager.crear_articulo("Articulo para Comentarios")
        self.manager.agregar_comentario(articulo.id, "Comentario 1")
        self.manager.agregar_comentario(articulo.id, "Comentario 2")
        comentarios = self.manager.leer_comentarios(articulo.id)
        self.assertEqual(len(comentarios), 2)
        self.assertEqual(comentarios[0].comentario, "Comentario 1")
        self.assertEqual(comentarios[1].comentario, "Comentario 2")


if __name__ == "__main__":
    unittest.main()
