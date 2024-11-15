from flask import (Flask, config, render_template, request, flash, json, send_file, session, jsonify, redirect, url_for) # type: ignore
from controllers.car_controller import CarController

app = Flask(__name__)
app.secret_key = "mvcflaskpython"

@app.route('/')
def main():
    return CarController.show_cars()

@app.route('/addcarros', methods=['POST', 'GET'])
def addcarros():
    if request.method == 'POST':
        CarController.insertCars()
    return redirect(url_for('main'))

@app.route('/viewcarros', methods=['POST', 'GET']) 
def viewcarros():
    if request.method == 'POST':
        # Llama a la función para visualizar los carros
        cars_data = CarController.viewCars()  # Almacena el resultado en una variable
        if cars_data is None:
            # Devuelve un error si no hay datos
            return jsonify({"error": "No data returned from viewCars"}), 500
        return cars_data  # Asegúrate de que sea un objeto de respuesta válido, como jsonify o render_template
    else:
        # Maneja la solicitud GET devolviendo una página o un mensaje
        return render_template('viewcarros.html')  # Asegúrate de tener el archivo viewcarros.html

@app.route('/deletecarros/<string:id>', methods=['POST', 'GET']) 
def deletecarros(id): 
    if request.method == 'GET': 
       CarController.deleteCars(id)
    return redirect(url_for('main'))

@app.route('/updatecarros', methods=['GET', 'POST']) 
def updatecarros(): 
    if request.method == 'POST':
        CarController.updateCarros()
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
    
