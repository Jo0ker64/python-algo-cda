function calculerMoyenne() {
    const notes = prompt("Entrez les notes séparées par des espaces : ").split(' ').map(Number);
    const moyenne = notes.reduce((acc, note) => acc + note, 0) / notes.length;
    alert("La moyenne est : " + moyenne);
}
