function sommeNombresPairs() {
    const liste = prompt("Entrez une liste de nombres séparés par des espaces : ").split(' ').map(Number);
    const somme = liste.reduce((acc, num) => num % 2 === 0 ? acc + num : acc, 0);
    alert("La somme des nombres pairs est : " + somme);
}
