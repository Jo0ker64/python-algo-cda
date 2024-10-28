function estPalindrome() {
    const mot = prompt("Entrez un mot : ").toLowerCase();
    alert(mot === mot.split('').reverse().join('') ? "C'est un palindrome" : "Ce n'est pas un palindrome");
}
