function plusGrandElement() {
    const liste = prompt("Entrez une liste de nombres séparés par des espaces : ").split(' ').map(Number);
    alert("Le plus grand élément est : " + Math.max(...liste));
}
