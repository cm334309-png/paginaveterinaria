from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# ===========================
# Base de datos
# ===========================

def crear_bd():

    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            correo TEXT,
            telefono TEXT,
            mascota TEXT,
            especie TEXT,
            mensaje TEXT
        )
    """)

    conexion.commit()
    conexion.close()

crear_bd()


# ===========================
# Página principal
# ===========================

@app.route("/")
def inicio():
    return render_template("index.html")


# ===========================
# Mascotas
# ===========================

@app.route("/mascotas", methods=["GET"])
def obtener_mascotas():

    mascotas = [

        {
            "id":1,
            "nombre":"Perros",
            "descripcion":"Atención médica, vacunas, peluquería y accesorios para perros.",
            "imagen":"https://images.unsplash.com/photo-1517849845537-4d257902454a"
        },

        {
            "id":2,
            "nombre":"Gatos",
            "descripcion":"Consulta veterinaria, vacunas y cuidado especializado para gatos.",
            "imagen":"https://images.unsplash.com/photo-1519052537078-e6302a4968d4"
        },

        {
            "id":3,
            "nombre":"Aves",
            "descripcion":"Revisión médica y control preventivo para aves domésticas.",
            "imagen":"https://images.unsplash.com/photo-1444464666168-49d633b86797"
        },

        {
            "id":4,
            "nombre":"Conejos",
            "descripcion":"Consulta, nutrición y control de salud para conejos.",
            "imagen":"https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308"
        },

        {
            "id":5,
            "nombre":"Hámsters",
            "descripcion":"Atención veterinaria para pequeños roedores.",
            "imagen":"https://images.unsplash.com/photo-1425082661705-1834bfd09dca"
        }

    ]

    return jsonify(mascotas)

# ===========================
# Servicios
# ===========================

@app.route("/servicios", methods=["GET"])
def obtener_servicios():

    servicios = [

        {
            "id":1,
            "nombre":"Consulta General",
            "descripcion":"Evaluación médica completa para tu mascota.",
            "precio":"50000",
            "imagen":"https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def"
        },

        {
            "id":2,
            "nombre":"Vacunación",
            "descripcion":"Aplicación de vacunas para prevenir enfermedades.",
            "precio":"35000",
            "imagen":"https://images.unsplash.com/photo-1583337130417-3346a1be7dee"
        },

        {
            "id":3,
            "nombre":"Desparasitación",
            "descripcion":"Protege la salud de tu mascota con tratamientos preventivos.",
            "precio":"30000",
            "imagen":"https://images.unsplash.com/photo-1517849845537-4d257902454a"
        },

        {
            "id":4,
            "nombre":"Peluquería",
            "descripcion":"Baño, corte de pelo y limpieza especializada.",
            "precio":"45000",
            "imagen":"https://images.unsplash.com/photo-1518717758536-85ae29035b6d"
        },

        {
            "id":5,
            "nombre":"Cirugía",
            "descripcion":"Procedimientos quirúrgicos con profesionales especializados.",
            "precio":"180000",
            "imagen":"https://images.unsplash.com/photo-1576201836106-db1758fd1c97"
        },

        {
            "id":6,
            "nombre":"Hospitalización",
            "descripcion":"Atención permanente para mascotas que requieren observación.",
            "precio":"120000",
            "imagen":"https://images.unsplash.com/photo-1450778869180-41d0601e046e"
        }

    ]

    return jsonify(servicios)


# ===========================
# Registrar cliente
# ===========================

@app.route("/clientes", methods=["POST"])
def registrar():

    datos = request.get_json()

    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO clientes
        (nombre,correo,telefono,mascota,especie,mensaje)
        VALUES (?,?,?,?,?,?)
    """,(

        datos["nombre"],
        datos["correo"],
        datos["telefono"],
        datos["mascota"],
        datos["especie"],
        datos["mensaje"]

    ))

    conexion.commit()
    conexion.close()

    return jsonify({"mensaje":"Cita registrada correctamente."})
# ===========================
# Listar clientes
# ===========================

@app.route("/clientes", methods=["GET"])
def listar():

    conexion = sqlite3.connect("clientes.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes")

    datos = cursor.fetchall()

    conexion.close()

    lista = []

    for fila in datos:

        lista.append({

            "id": fila[0],
            "nombre": fila[1],
            "correo": fila[2],
            "telefono": fila[3],
            "mascota": fila[4],
            "especie": fila[5],
            "mensaje": fila[6]

        })

    return jsonify(lista)


# ===========================
# Iniciar aplicación
# ===========================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5003))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )