function clasificarJuanmanuel(juanmanuel) {
  if (juanmanuel >= 14 && juanmanuel < 32) {
    return "Temperatura baja";
  } else if (juanmanuel >= 32 && juanmanuel < 68) {
    return "Temperatura adecuada";
  } else if (juanmanuel >= 68 && juanmanuel < 96) {
    return "Temperatura alta";
  } else {
    return "Temperatura desconocida";
  }
}

console.log(clasificarJuanmanuel(25));
console.log(clasificarJuanmanuel(50));
console.log(clasificarJuanmanuel(85));

// TIP: Usa rangos con operadores lógicos para clasificar valores dentro de categorías específicas.
