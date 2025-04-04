const resultadosTotales = [];

document.getElementById("lifeWheelForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const salud = document.getElementById("salud").value;
    const finanzas = document.getElementById("finanzas").value;
    const relaciones = document.getElementById("relaciones").value;
    const trabajo = document.getElementById("trabajo").value;

    const nuevoResultado = {
        salud,
        finanzas,
        relaciones,
        trabajo
    };

    resultadosTotales.push(nuevoResultado);
    mostrarResultados();
});

function mostrarResultados() {
    const resultados = document.getElementById("resultados");
    resultados.innerHTML = "";

    resultadosTotales.forEach((resultado, index) => {
        const resultadoHTML = `
            <div class="resultado-item">
                <h3>Registro ${index + 1}</h3>
                <p><strong>Salud:</strong> ${resultado.salud}</p>
                <p><strong>Finanzas:</strong> ${resultado.finanzas}</p>
                <p><strong>Relaciones:</strong> ${resultado.relaciones}</p>
                <p><strong>Trabajo:</strong> ${resultado.trabajo}</p>
                <hr>
            </div>
        `;
        resultados.innerHTML += resultadoHTML;
    });
}
