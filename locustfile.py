from locust import HttpUser, task, between # type: ignore

class WebsiteUser(HttpUser):
    # Define el tiempo de espera entre cada tarea que realiza el usuario (en segundos)
    wait_time = between(1, 3)

    @task
    def main_page(self):
        # Simula una solicitud GET a la página principal
        self.client.get("/")

    @task
    def add_carros(self):
        # Simula una solicitud POST para agregar un carro (se puede ajustar según los campos necesarios)
        self.client.post("/addcarros", json={"name": "Nuevo Carro", "model": "2024", "price": 15000})

    @task
    def view_carros(self):
        # Simula una solicitud POST a la vista de carros
        self.client.post("/viewcarros")

    @task
    def delete_carros(self):
        # Simula una solicitud GET para eliminar un carro con un ID de ejemplo
        # Cambia "1" por un ID de prueba válido si tienes un ID específico
        self.client.get("/deletecarros/1")

    @task
    def update_carros(self):
        # Simula una solicitud POST para actualizar un carro (ajusta los datos según tus requisitos)
        self.client.post("/updatecarros", json={"id": "1", "name": "Carro Actualizado", "model": "2023", "price": 16000})
