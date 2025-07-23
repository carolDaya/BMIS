from flask import Flask, request, jsonify
from flask_cors import CORS  # Para conexión Android
import joblib
import numpy as np
import random

# Carga del modelo
model = joblib.load('biodigestor_model.pkl')

# Configuración Flask
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '¡Backend Biodigestor funcionando!'


@app.route('/obtener_estado_biodigestor', methods=['POST'])
def obtener_estado_biodigestor():
    if not request.is_json:
        return jsonify({"error": "La petición debe ser JSON"}), 400

    data = request.get_json()

    required_fields = ['temperatura', 'presion', 'mq4_gas']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo '{field}'"}), 400

    try:
        temp = float(data['temperatura'])
        pres = float(data['presion'])
        gas = float(data['mq4_gas'])
    except ValueError:
        return jsonify({"error": "Valores inválidos"}), 400

    # Predicción del modelo
    input_data = np.array([[temp, pres, gas]])
    prediction = model.predict(input_data)[0]

    # Verificación con reglas
    recomendaciones = []

    if temp < 15:
        opciones_temp_baja = [
            "Temperatura baja: Aísle con lona o paja.",
            "Temperatura baja: Instale techo para proteger del frío.",
            "Temperatura baja: Use agua caliente si es posible."
        ]
        recomendaciones.append(random.choice(opciones_temp_baja))
    elif temp > 37:
        opciones_temp_alta = [
            "Temperatura alta: Instale sombra o malla.",
            "Temperatura alta: Aumente ventilación.",
            "Temperatura alta: Riegue agua alrededor para enfriar."
        ]
        recomendaciones.append(random.choice(opciones_temp_alta))

    if pres < 0.7:
        opciones_pres_baja = [
            "Presión baja: Revise mangueras y uniones.",
            "Presión baja: Verifique nivel de lodos.",
            "Presión baja: Inspeccione fisuras en la estructura."
        ]
        recomendaciones.append(random.choice(opciones_pres_baja))
    elif pres > 1.5:
        opciones_pres_alta = [
            "Presión alta: Libere gas acumulado.",
            "Presión alta: Limpie válvulas y tuberías.",
            "Presión alta: Verifique obstrucciones por residuos."
        ]
        recomendaciones.append(random.choice(opciones_pres_alta))

    if gas > 200:
        opciones_gas_alto = [
            "Gas elevado: Ventile bien el área.",
            "Gas elevado: Revise sellos y uniones.",
            "Gas elevado: Evite fuego o chispas cerca."
        ]
        recomendaciones.append(random.choice(opciones_gas_alto))

    # Si hay recomendaciones → alerta. Si no → normal.
    if len(recomendaciones) > 0:
        status_message = "Alerta"
        full_message = (
            "Atención: Se detectaron problemas:\n"
            + "\n".join(f"- {rec}" for rec in recomendaciones)
        )
    else:
        status_message = "Normal"
        full_message = (
            "El biodigestor funciona correctamente.\n"
            "No se detectaron problemas.\n"
            "Continúe monitoreando temperatura, presión y nivel de gas periódicamente."
        )

    return jsonify({
        "status": status_message,
        "message": full_message
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
