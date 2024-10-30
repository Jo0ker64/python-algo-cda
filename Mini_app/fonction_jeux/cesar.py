print("Lancement du Codeur/Décodeur César ...")

def coder_cesar(message, decalage):
    """
    Code un message avec le chiffrement de César.
    
    :param message: Le message à coder
    :param decalage: Le nombre de positions de décalage à utiliser pour le chiffrement
    :return: Le message codé
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message_code = ''

    for caractere in message.upper():
        if caractere in alphabet:
            index = alphabet.index(caractere)
            nouvelle_position = (index + decalage) % 26
            message_code += alphabet[nouvelle_position]
        else:
            message_code += caractere

    return message_code

def decoder_cesar(message, decalage):
    """
    Décode un message chiffré avec le chiffrement de César.
    
    :param message: Le message chiffré à décoder
    :param decalage: Le nombre de positions de décalage utilisé pour le chiffrement
    :return: Le message décodé
    """
    return coder_cesar(message, -decalage)  # Le décodage est un codage avec un décalage négatif

def cesar():
    print("Bienvenue dans le codeur/décodeur César!")
    
    while True:
        choix = input("Voulez-vous coder (C) ou décoder (D) un message ? (ou 'Q' pour quitter): ").upper()
        if choix == 'Q':
            break
        elif choix not in ['C', 'D']:
            print("Choix invalide. Veuillez entrer 'C', 'D' ou 'Q'.")
            continue

        message = input("Entrez le message : ")

        try:
            decalage = int(input("Entrez le décalage : "))
        except ValueError:
            print("Erreur : Le décalage doit être un nombre entier.")
            continue

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
