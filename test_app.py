import unittest
from app import app  # Importa la aplicación Flask desde el archivo principal
from flask import url_for

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Configura la aplicación para el contexto de prueba
        self.app = app.test_client()
        self.app.testing = True

    # Prueba la ruta principal
    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Verifica que el código de estado sea 200

    # Prueba la ruta para agregar carros
    def test_addcarros_route_get(self):
        # Prueba la respuesta cuando se accede a la ruta con GET
        response = self.app.get('/addcarros')
        self.assertEqual(response.status_code, 302)  # Redirecciona a la página principal

    def test_addcarros_route_post(self):
        # Prueba la respuesta cuando se accede a la ruta con POST
        response = self.app.post('/addcarros', data={
            'nombre': 'Carro Prueba',
            'modelo': 'Modelo Prueba'
        })
        self.assertEqual(response.status_code, 302)  # Verifica redirección a la página principal

    # Prueba la ruta para visualizar carros
    def test_viewcarros_route_post(self):
        # Prueba la respuesta cuando se accede a la ruta con POST
        response = self.app.post('/viewcarros')
        self.assertEqual(response.status_code, 200)

    def test_viewcarros_route_get(self):
        # Prueba la respuesta cuando se accede a la ruta con GET
        response = self.app.get('/viewcarros')
        self.assertEqual(response.status_code, 200)

    # Prueba la ruta para eliminar carros
    def test_deletecarros_route_get(self):
        # Prueba la eliminación con un ID ficticio
        response = self.app.get('/deletecarros/1')  # "1" es un ID de prueba
        self.assertEqual(response.status_code, 302)  # Verifica redirección a la página principal

    # Prueba la ruta para actualizar carros
    def test_updatecarros_route_post(self):
        # Prueba la actualización con datos de prueba
        response = self.app.post('/updatecarros', data={
            'id': '1',
            'nombre': 'Carro Actualizado',
            'modelo': 'Modelo Actualizado'
        })
        self.assertEqual(response.status_code, 302)  # Verifica redirección a la página principal

    def test_updatecarros_route_get(self):
        # Prueba la respuesta cuando se accede a la ruta con GET
        response = self.app.get('/updatecarros')
        self.assertEqual(response.status_code, 302)  # Redirecciona a la página principal

if __name__ == '__main__':
    unittest.main()
