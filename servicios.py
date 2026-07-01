from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def inicio():
    return "<h2>Microservicio de Servicios funcionando correctamente.</h2>"

@app.route("/servicios", methods=["GET"])
def obtener_servicios():

    servicios = [

        {
            "id": 1,
            "nombre": "Consulta General",
            "descripcion": "Evaluación médica completa para tu mascota.",
            "precio": "50000",
            "imagen": "https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def"
        },

        {
            "id": 2,
            "nombre": "Vacunación",
            "descripcion": "Aplicación de vacunas para prevenir enfermedades.",
            "precio": "35000",
            "imagen": "https://images.unsplash.com/photo-1583337130417-3346a1be7dee"
        },

        {
            "id": 3,
            "nombre": "Desparasitación",
            "descripcion": "Protege la salud de tu mascota con tratamientos preventivos.",
            "precio": "30000",
            "imagen": "https://images.unsplash.com/photo-1517849845537-4d257902454a"
        },

        {
            "id": 4,
            "nombre": "Peluquería",
            "descripcion": "Baño, corte de pelo y limpieza especializada.",
            "precio": "45000",
            "imagen": "https://images.unsplash.com/photo-1518717758536-85ae29035b6d"
        },

        {
            "id": 5,
            "nombre": "Cirugía",
            "descripcion": "Procedimientos quirúrgicos con profesionales especializados.",
            "precio": "180000",
            "imagen": "https://images.unsplash.com/photo-1576201836106-db1758fd1c97"
        },

        {
            "id": 6,
            "nombre": "Hospitalización",
            "descripcion": "Atención permanente para mascotas que requieren observación.",
            "precio": "120000",
            "imagen": "https://images.unsplash.com/photo-1450778869180-41d0601e046e"
        }

    ]

    return jsonify(servicios)

if __name__ == "__main__":
    print("Microservicio de Servicios iniciado correctamente...")
    app.run(host="127.0.0.1", port=5002, debug=True)