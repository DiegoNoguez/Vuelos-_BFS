    const form = document.getElementById('formulario');
    const resultado = document.getElementById('resultado');
    const tabla = document.getElementById('tabla-rutas');

    //  Conexiones (mismas del backend)
    const conexiones = {
        'JILOYORK': ['CELAYA', 'CDMX', 'QUERÉTARO'],
        'SONORA': ['ZACATECAS', 'SINALOA'],
        'GUANAJUATO': ['AGUASCALIENTES'],
        'OAXACA': ['QUERÉTARO'],
        'SINALOA': ['CELAYA', 'SONORA', 'JILOYORK'],
        'CDMX': ['MONTERREY'],
        'CELAYA': ['JILOYORK', 'SINALOA'],
        'ZACATECAS': ['SONORA', 'MONTERREY', 'QUERÉTARO'],
        'MONTERREY': ['ZACATECAS'],
        'TAMAULIPAS': ['QUERÉTARO'],
        'QUERÉTARO': ['TAMAULIPAS', 'ZACATECAS', 'SINALOA', 'JILOYORK', 'OAXACA']
    };

    //  Cargar tabla automáticamente
    function cargarTabla() {
        for (let ciudad in conexiones) {
            const fila = document.createElement('tr');

            fila.innerHTML = `
                <td class="border p-2 font-semibold text-purple-700">${ciudad}</td>
                <td class="border p-2 text-emerald-700">${conexiones[ciudad].join(", ")}</td>
            `;

            tabla.appendChild(fila);
        }
    }

    cargarTabla();


    //  Consumo API
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const inicio = document.getElementById('inicio').value.trim();
        const destino = document.getElementById('destino').value.trim();

        resultado.textContent = "Buscando...";

        try {
            const response = await fetch(API_URL + "buscar-ruta/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    inicio: inicio,
                    destino: destino
                })
            });

            const data = await response.json();

            if (data.encontrado) {
                resultado.textContent = "Ruta: " + data.ruta.join(" → ");
            } else {
                resultado.textContent = "No se encontró ruta";
            }

        } catch (error) {
            resultado.textContent = "Error al conectar con la API";
            console.error(error);
        }
    });