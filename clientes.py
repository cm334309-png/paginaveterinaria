from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

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


@app.route("/clientes", methods=["POST"])
def registrar():

    datos = request.get_json()

    conexion = sqlite3.connect("clientes.db")

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO clientes
        (nombre,correo,telefono,mascota,especie,mensaje)
        VALUES(?,?,?,?,?,?)
    """, (
        datos["nombre"],
        datos["correo"],
        datos["telefono"],
        datos["mascota"],
        datos["especie"],
        datos["mensaje"]
    ))

    conexion.commit()
    conexion.close()

    return jsonify({"mensaje": "Cita registrada correctamente."})


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


@app.route("/")
def inicio():
    return "Microservicio de Clientes funcionando correctamente."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port)