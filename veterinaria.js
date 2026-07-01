// ==========================================
// CAMS VETERINARIA
// veterinaria.js
// ==========================================

// Cargar mascotas
async function cargarMascotas() {

    try {

        const respuesta = await fetch("http://127.0.0.1:5001/mascotas");

        const mascotas = await respuesta.json();

        const contenedor = document.getElementById("listaMascotas");

        contenedor.innerHTML = "";

        mascotas.forEach(mascota => {

            contenedor.innerHTML += `

                <div class="card">

                    <img src="${mascota.imagen}" alt="${mascota.nombre}">

                    <h3>${mascota.nombre}</h3>

                    <p>${mascota.descripcion}</p>

                    <button>Más información</button>

                </div>

            `;

        });

    } catch (error) {

        console.error("Error al cargar las mascotas:", error);

    }

}

// ==========================================
// Cargar servicios
// ==========================================

async function cargarServicios() {

    try {

        const respuesta = await fetch("http://127.0.0.1:5002/servicios");

        const servicios = await respuesta.json();

        const contenedor = document.getElementById("listaServicios");

        contenedor.innerHTML = "";

        servicios.forEach(servicio => {

            contenedor.innerHTML += `

                <div class="card">

                    <img src="${servicio.imagen}" alt="${servicio.nombre}">

                    <h3>${servicio.nombre}</h3>

                    <p>${servicio.descripcion}</p>

                    <button>$ ${servicio.precio}</button>

                </div>

            `;

        });

    } catch (error) {

        console.error("Error al cargar los servicios:", error);

    }

}

// ==========================================
// Registrar cita
// ==========================================

const formulario = document.getElementById("formCliente");

formulario.addEventListener("submit", async function(e){

    e.preventDefault();

    const datos = {

        nombre: document.getElementById("nombre").value,

        correo: document.getElementById("correo").value,

        telefono: document.getElementById("telefono").value,

        mascota: document.getElementById("mascota").value,

        especie: document.getElementById("especie").value,

        mensaje: document.getElementById("mensaje").value

    };

    try{

        const respuesta = await fetch("http://127.0.0.1:5003/clientes",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify(datos)

        });

        const resultado = await respuesta.json();

        alert(resultado.mensaje);

        formulario.reset();

    }

    catch(error){

        alert("No fue posible registrar la cita.");

        console.error(error);

    }

});

// ==========================================
// Iniciar aplicación
// ==========================================

cargarMascotas();

cargarServicios();
