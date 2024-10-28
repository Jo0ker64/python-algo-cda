let nombre = parseInt(prompt("Entrez un nombre entre 1 et 100 : "));

while (isNaN(nombre) || nombre < 1 || nombre > 100) {
    alert("Le nombre doit être compris entre 1 et 100.");
    nombre = parseInt(prompt("Entrez un nombre entre 1 et 100 : "));
}

console.log("Nombre valide saisi :", nombre);
