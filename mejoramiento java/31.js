let juanmanuel1 = [];

function agregarTarea(lista, tarea) {
  const juanmanuel2 = [...lista, tarea];
  console.log(`Tarea agregada: "${tarea}"`);
  return juanmanuel2;
}

function completarTarea(lista, indice) {
  if (indice >= 0 && indice < lista.length) {
    const juanmanuel2 = lista.map((t, i) =>
      i === indice ? "7 " + t : t
    );
    console.log("Tarea marcada como completada");
    return juanmanuel2;
  } else {
    console.log("Índice inválido");
    return lista;
  }
}

function obtenerEstadisticas(lista) {
  const total = lista.length;
  const completadas = lista.filter(t => t.startsWith("7")).length;
  const pendientes = total - completadas;
  return { total, completadas, pendientes };
}

function mostrarTareas(lista) {
  console.log("\n=== LISTA DE TAREAS ===");
  lista.forEach((tarea, i) => {
    console.log(`${i}. ${tarea}`);
  });
}

juanmanuel1 = agregarTarea(juanmanuel1, "Estudiar JavaScript");
juanmanuel1 = agregarTarea(juanmanuel1, "Hacer ejercicio");
juanmanuel1 = agregarTarea(juanmanuel1, "Preparar presentación");

mostrarTareas(juanmanuel1);

juanmanuel1 = completarTarea(juanmanuel1, 0);

mostrarTareas(juanmanuel1);

const stats = obtenerEstadisticas(juanmanuel1);
console.log("\n=== ESTADÍSTICAS ===");
console.log(`Total: ${stats.total}`);
console.log(`Completadas: ${stats.completadas}`);
console.log(`Pendientes: ${stats.pendientes}`);
