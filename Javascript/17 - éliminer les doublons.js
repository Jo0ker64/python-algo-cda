let liste = [1, 2, 3, 1, 2, 4, 5, 3, 6];  // Exemple de liste avec des doublons
let nouvelleListe = [];

for (let i = 0; i < liste.length; i++) {
    if (!nouvelleListe.includes(liste[i])) {
        nouvelleListe.push(liste[i]);
    }
}

console.log("Liste sans doublons :", nouvelleListe);
