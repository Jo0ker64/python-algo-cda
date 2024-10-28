// Demande à l'utilisateur d'entrer une chaîne de caractères
const chaine = prompt("Entrez une chaîne de caractères : ");

// Fonction pour inverser la chaîne
function inverserChaine(str) {
    // Utilise split pour convertir la chaîne en tableau, reverse pour inverser le tableau, 
    // et join pour reconvertir le tableau en chaîne
    return str.split('').reverse().join('');
}

// Inverse la chaîne et l'affiche
const chaineInversee = inverserChaine(chaine);
console.log("La chaîne inversée est :", chaineInversee);
