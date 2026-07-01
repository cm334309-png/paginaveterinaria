from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/mascotas', methods=['GET'])
def obtener_mascotas():

    mascotas = [

        {
            "id": 1,
            "nombre": "Perros",
            "descripcion": "Atención médica, vacunas, peluquería y accesorios para perros.",
            "imagen": "https://images.unsplash.com/photo-1517849845537-4d257902454a"
        },

        {
            "id": 2,
            "nombre": "Gatos",
            "descripcion": "Consulta veterinaria, vacunas y cuidado especializado para gatos.",
            "imagen": "https://images.unsplash.com/photo-1519052537078-e6302a4968d4"
        },

        {
            "id": 3,
            "nombre": "Aves",
            "descripcion": "Revisión médica y control preventivo para aves domésticas.",
            "imagen": "https://images.unsplash.com/photo-1444464666168-49d633b86797"
        },

        {
            "id": 4,
            "nombre": "Conejos",
            "descripcion": "Consulta, nutrición y control de salud para conejos.",
            "imagen": "https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308"
        },

        {
            "id": 5,
            "nombre": "Hámsters",
            "descripcion": "Atención veterinaria para pequeños roedores.",
            "imagen": "https://images.unsplash.com/photo-1425082661705-1834bfd09dca"
        }

    ]

    return jsonify(mascotas)

@app.route('/')
def inicio():
    return "<h2>Microservicio de Mascotas funcionando correctamente.</h2>"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
