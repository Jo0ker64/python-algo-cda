print("Lancement du Codeur/Décodeur César ...")

def coder_cesar(message, decalage):
    """
    Cette fonction code un message avec le chiffrement de César.
    Elle prend en entrée le message et le décalage, et retourne le message codé.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message_code = ''

    for caractere in message.upper():
        if caractere in alphabet:
            # Trouve la nouvelle position de la lettre dans l'alphabet
            index = alphabet.index(caractere)
            nouvelle_position = (index + decalage) % 26
            message_code += alphabet[nouvelle_position]
        else:
            # Conserve les caractères non alphabétiques tels quels
            message_code += caractere

    return message_code

def decoder_cesar(message, decalage):
    """
    Cette fonction décode un message chiffré avec César.
    Elle utilise la fonction de codage avec un décalage négatif.
    """
    return coder_cesar(message, -decalage)

def cesar():
    print("Bienvenue dans le codeur/décodeur César!")
    
    while True:
        # Demande à l'utilisateur s'il veut coder ou décoder
        choix = input("Voulez-vous coder (C) ou décoder (D) un message ? (ou 'Q' pour quitter): ").upper()
        if choix == 'Q':
            break
        elif choix not in ['C', 'D']:
            print("Choix invalide. Veuillez entrer 'C', 'D' ou 'Q'.")
            continue

        # Demande le message à traiter
        message = input("Entrez le message : ")

        # Demande le décalage et vérifie qu'il s'agit bien d'un nombre
        try:
            decalage = int(input("Entrez le décalage : "))
        except ValueError:
            print("Erreur : Le décalage doit être un nombre entier.")
            continue

        # Applique le codage ou le décodage selon le choix
        if choix == 'C':
            resultat = coder_cesar(message, decalage)
            print(f"Message codé : {resultat}")
        else:  # choix == 'D'
            resultat = decoder_cesar(message, decalage)
            print(f"Message décodé : {resultat}")
        
        print()

    print("Merci d'avoir utilisé le codeur/décodeur César!")

if __name__ == "__main__":
    cesar()
