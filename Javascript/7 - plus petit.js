function plusPetitElement() {
    const liste = prompt("Entrez une liste de nombres séparés par des espaces : ").split(' ').map(Number);
    alert("Le plus petit élément est : " + Math.min(...liste));
}
