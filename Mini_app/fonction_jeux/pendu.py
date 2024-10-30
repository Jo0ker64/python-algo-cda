print("Lancement du Jeu du pendu ...")

import random

def choisir_mot():
    mots = ["python", "ordinateur", "programmation", "intelligence", "algorithme"]
    return random.choice(mots).upper()

def afficher_mot(mot, lettres_trouvees):
    affichage = [lettre if lettre in lettres_trouvees else "_" for lettre in mot]
    return " ".join(affichage)

def pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    essais_restants = 6
    lettres_essayees = set()

    print("Bienvenue au jeu du pendu !")
    
    while essais_restants > 0:
        print("\nMot à deviner :", afficher_mot(mot_a_deviner, lettres_trouvees))
        print("Lettres essayées :", " ".join(sorted(lettres_essayees)))
        print("Essais restants :", essais_restants)

        lettre = input("Proposez une lettre : ").upper()

        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue

        lettres_essayees.add(lettre)

        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print("Bonne lettre !")
        else:
            essais_restants -= 1
            print("Mauvaise lettre.")

        if all(l in lettres_trouvees for l in mot_a_deviner):
            print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
            break
    else:
        print("\nVous avez perdu ! Le mot était :", mot_a_deviner)

# Lancer le jeu
pendu()