function calculerPrixPhotocopies() {
    const nombrePhotocopies = parseInt(prompt("Entrez le nombre de photocopies : "));
    let prix;
    if (nombrePhotocopies <= 10) {
        prix = nombrePhotocopies * 0.20;
    } else if (nombrePhotocopies <= 30) {
        prix = 10 * 0.20 + (nombrePhotocopies - 10) * 0.15;
    } else {
        prix = 10 * 0.20 + 20 * 0.15 + (nombrePhotocopies - 30) * 0.10;
    }
    alert("Le prix total est : " + prix.toFixed(2) + " €");
}
