function calculerPrixHT() {
    const prixTTC = parseFloat(prompt("Entrez le prix TTC : "));
    const prixHT = prixTTC / 1.20;
    alert("Le prix HT est : " + prixHT.toFixed(2) + " €");
}
