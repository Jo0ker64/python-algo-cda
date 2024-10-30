print("Lancement du Jeu du pendu ...")

import random

def choisir_mot():
    # Liste de mots possibles pour le jeu
    mots = ["python", "ordinateur", "programmation", "intelligence", "algorithme"]
    # Choix aléatoire d'un mot et conversion en majuscules
    return random.choice(mots).upper()

def afficher_mot(mot, lettres_trouvees):
    # Crée une liste où chaque lettre du mot est affichée si elle a été trouvée, sinon un "_"
    affichage = [lettre if lettre in lettres_trouvees else "_" for lettre in mot]
    # Convertit la liste en chaîne de caractères avec des espaces entre chaque lettre/underscore
    return " ".join(affichage)

def pendu():
    # Sélectionne un mot aléatoire à deviner
    mot_a_deviner = choisir_mot()
    # Ensemble pour stocker les lettres correctement devinées
    lettres_trouvees = set()
    # Nombre d'essais autorisés
    essais_restants = 6
    # Ensemble pour stocker toutes les lettres essayées
    lettres_essayees = set()

    while essais_restants > 0:
        # Affiche l'état actuel du mot à deviner
        print("\nMot à deviner :", afficher_mot(mot_a_deviner, lettres_trouvees))
        # Affiche les lettres déjà essayées
        print("Lettres essayées :", " ".join(sorted(lettres_essayees)))
        # Affiche le nombre d'essais restants
        print("Essais restants :", essais_restants)

        # Demande à l'utilisateur de proposer une lettre
        lettre = input("Proposez une lettre : ").upper()

        # Vérifie si la lettre a déjà été essayée
        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue

        # Ajoute la lettre aux lettres essayées
        lettres_essayees.add(lettre)

        # Vérifie si la lettre est dans le mot
        if lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print("Bonne lettre !")
        else:
            essais_restants -= 1
            print("Mauvaise lettre.")

        # Vérifie si toutes les lettres du mot ont été trouvées
        if all(l in lettres_trouvees for l in mot_a_deviner):
            print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
            break
    else:
        # S'exécute si la boucle se termine normalement (essais épuisés)
        print("\nVous avez perdu ! Le mot était :", mot_a_deviner)

# Le code pour appeler la fonction pendu() n'est pas inclus ici
if __name__ == "__main__":
    pendu()