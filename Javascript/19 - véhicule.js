// Demander les informations à l'utilisateur
let annees_permis = parseInt(prompt("Nombre d'années de permis : "));
let nombre_accidents = parseInt(prompt("Nombre d'accidents : "));

// Initialiser la catégorie
let categorie = "Indéterminée";

// Vérifier les critères et attribuer la catégorie
if (annees_permis < 2 || nombre_accidents > 3) {
    categorie = "Rouge";
} else if (annees_permis < 5 && nombre_accidents >= 1 && nombre_accidents <= 2) {
    categorie = "Orange";
} else if (annees_permis >= 5 && nombre_accidents < 1) {
    categorie = "Vert";
} else if (annees_permis > 10 && nombre_accidents === 0) {
    categorie = "Bleu";
}

// Afficher le résultat
console.log(`La catégorie de l'assuré est : ${categorie}`);
