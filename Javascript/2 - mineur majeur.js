// Définition de la fonction verifierAge
function verifierAge() {
    // Demande à l'utilisateur d'entrer son âge via une boîte de dialogue
    // La saisie est convertie en nombre entier avec parseInt
    const age = parseInt(prompt("Entrez votre âge : "));

    // Vérifie si l'entrée n'est pas un nombre (NaN)
    if (isNaN(age)) {
        // Affiche un message d'alerte si l'utilisateur n'a pas entré un nombre valide
        alert("Veuillez entrer un nombre valide.");
    } else {
        // Utilise un opérateur ternaire pour vérifier si l'âge est supérieur ou égal à 18
        // Affiche "Majeur" si vrai, sinon "Mineur"
        alert(age >= 18 ? "Majeur" : "Mineur");
    }
}

// Appel immédiat de la fonction verifierAge pour exécuter le code
verifierAge();
