function nombreLePlusRepete() {
    const liste = prompt("Entrez une liste de nombres séparés par des espaces : ").split(' ').map(Number);
    const compteur = {};
    liste.forEach(num => {
        compteur[num] = (compteur[num] || 0) + 1;
    });
    const plusRepete = Object.keys(compteur).reduce((a, b) => compteur[a] > compteur[b] ? a : b);
    alert("Le nombre le plus répété est : " + plusRepete);
}
