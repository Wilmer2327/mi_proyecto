import mysql.connector  # type: ignore
from config import DATABASE_CONFIG
import logging

# Configuración de logging para errores
logging.basicConfig(level=logging.ERROR)

class CarModel:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(**DATABASE_CONFIG)
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            logging.error(f"Error connecting to MySQL: {err}")
            raise

    def get_all_cars(self):
        try:
            self.cursor.execute("SELECT * FROM tbclientes")
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            logging.error(f"Error fetching all cars: {err}")
            return []

    def insert_Cars(self, Idcliente, Nombre, Apellido1, Apellido2, Telefono):
        try:
            self.cursor.execute(
                'INSERT INTO tbclientes(Idcliente, Nombre, Apellido1, Apellido2, Telefono) VALUES(%s, %s, %s, %s, %s)',
                (Idcliente, Nombre, Apellido1, Apellido2, Telefono)
            )
            self.connection.commit()
        except mysql.connector.Error as err:
            logging.error(f"Error inserting car: {err}")
            self.connection.rollback()

    def get_one_cars(self, id):
        try:
            self.cursor.execute("SELECT * FROM tbclientes WHERE Idcliente = %s", [id])
            result = self.cursor.fetchone()  # Usamos fetchone si esperamos solo un registro
            return result
        except mysql.connector.Error as err:
            logging.error(f"Error fetching one car with id {id}: {err}")
            return None

    def delete_cars(self, id):
        try:
            self.cursor.execute('DELETE FROM tbclientes WHERE Idcliente = %s', (id,))
            self.connection.commit()
        except mysql.connector.Error as err:
            logging.error(f"Error deleting car with id {id}: {err}")
            self.connection.rollback()

    def update_Cars(self, Idcliente, Nombre, Apellido1, Apellido2, Telefono):
        try:
            self.cursor.execute(
                "UPDATE tbclientes SET Nombre=%s, Apellido1=%s, Apellido2=%s, Telefono=%s WHERE Idcliente = %s",
                (Nombre, Apellido1, Apellido2, Telefono, Idcliente)
            )
            self.connection.commit()
        except mysql.connector.Error as err:
            logging.error(f"Error updating car with id {Idcliente}: {err}")
            self.connection.rollback()

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except mysql.connector.Error as err:
            logging.error(f"Error closing connection: {err}")







