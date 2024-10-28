function nombreDeVoyelles() {
    const mot = prompt("Entrez un mot : ").toLowerCase();
    const voyelles = "aeiouy";
    let nombreVoyelles = 0;
    for (let lettre of mot) {
        if (voyelles.includes(lettre)) {
            nombreVoyelles++;
        }
    }
    alert("Nombre de voyelles : " + nombreVoyelles);
}
