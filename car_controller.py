from flask import (Flask, config, render_template, request, flash, json, send_file, session, jsonify, redirect, url_for) # type: ignore
from models.car_model import CarModel

class CarController:
    @staticmethod
    def show_cars():
        car_model = CarModel()
        tbclientes = car_model.get_all_cars()
        car_model.close()
        return render_template('index.html', tbclientes=tbclientes)

    @staticmethod
    def viewCars():
        try:
            # Lógica para obtener los carros de la base de datos o cualquier otro dato
            cars = CarModel().get_all_cars()  # Asegúrate de que esta función devuelva datos correctamente
            return render_template('viewcarros.html', cars=cars)
        except Exception as e:
            print(f"Error al obtener los carros: {e}")
            # En caso de error, podemos retornar una página de error o un mensaje
            flash('Error al cargar los carros. Intenta nuevamente.', 'error')
            return redirect(url_for('main'))

    @staticmethod
    def insertCars():
        try:
            car_model = CarModel()
            Idcliente = request.form['Idcliente'] 
            Nombre = request.form['Nombre'] 
            Apellido1 = request.form['Apellido1'] 
            Apellido2 = request.form['Apellido2'] 
            Telefono = request.form['Telefono'] 
            car_model.insert_Cars(Idcliente, Nombre, Apellido1, Apellido2, Telefono)
            car_model.close()
            flash('Cliente registrado correctamente!!!')      
        except Exception as e:
            print(f"Error en insertCars: {e}")
            flash('¡Ha ocurrido un error!')

    @staticmethod
    def deleteCars(id):
        try:
            car_model = CarModel()
            car_model.delete_cars(id)
            car_model.close()
            flash('Cliente eliminado correctamente!!!') 
        except Exception as e:
            print(f"Error en deleteCars: {e}")
            flash('¡Ha ocurrido un error!')

    @staticmethod
    def updateCarros():
        try:
            car_model = CarModel()
            Idcliente = request.form['id'] 
            Nombre = request.form['Nombre'] 
            Apellido1 = request.form['Apellido1'] 
            Apellido2 = request.form['Apellido2'] 
            Telefono = request.form['Telefono'] 
            car_model.update_Cars(Idcliente, Nombre, Apellido1, Apellido2, Telefono)
            car_model.close()
            flash('Cliente actualizado correctamente!!!')      
        except Exception as e:
            print(f"Error en updateCarros: {e}")
            flash('¡Ha ocurrido un error!')
