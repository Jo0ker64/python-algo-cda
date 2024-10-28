function tableMultiplication() {
    const nombre = parseInt(prompt("Entrez un nombre pour afficher sa table de multiplication : "));
    let result = "";
    for (let i = 1; i <= 10; i++) {
        result += `${nombre} x ${i} = ${nombre * i}\n`;
    }
    alert(result);
}
