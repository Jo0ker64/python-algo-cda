// Demande à l'utilisateur d'entrer un nombre
// prompt() affiche une boîte de dialogue et récupère la saisie de l'utilisateur
// parseInt() convertit la saisie (qui est une chaîne) en un entier
let nombre = parseInt(prompt("Entrez un nombre : "));

// Vérifie si le nombre est pair
// L'opérateur % calcule le reste de la division par 2
// Si ce reste est 0, le nombre est pair
if (nombre % 2 === 0) {
    // Si la condition est vraie (le nombre est pair), affiche "pair"
    console.log("pair");
} else {
    // Si la condition est fausse (le nombre est impair), affiche "impair"
    console.log("impair");
}
