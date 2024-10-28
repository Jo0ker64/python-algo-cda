// Demande à l'utilisateur d'entrer le premier nombre
// prompt() affiche une boîte de dialogue et renvoie la saisie de l'utilisateur sous forme de chaîne
// parseFloat() convertit cette chaîne en nombre décimal
const num1 = parseFloat(prompt("Entrez le premier nombre : "));

// Demande à l'utilisateur d'entrer le second nombre
// Même processus que pour num1
const num2 = parseFloat(prompt("Entrez le second nombre : "));

// Affiche une boîte d'alerte avec la somme des deux nombres
// (num1 + num2) calcule la somme
// Le résultat est converti en chaîne et concaténé avec le message
alert("La somme est : " + (num1 + num2));
