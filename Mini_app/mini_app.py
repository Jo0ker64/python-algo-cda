# Importer les fichiers
# from nomDuDossier.mon_document import le ou les éléments que je souhaites utilisé

from fonction_jeux.remise import calcul_remise
from fonction_jeux.dés import jeu_de_des
from fonction_jeux.prix import juste_prix
from fonction_jeux.horloge import horloge
from fonction_jeux.pendu import pendu
from fonction_jeux.cesar import cesar
from fonction_jeux.contact import contact

# Définition de la fonction pour afficher le menu principal
def affiche_menu():
    # Affichage du menu avec différentes options
    print("**************************************")
    print("Menu de l'application :")
    print("0. Quitter")
    print("1. Calculer une remise en %")
    print("2. Lancé de dé")
    print("3. Jeu du juste prix")
    print("4. Horloge numérique (HH:MM:SS qui défile)")
    print("5. Jeu du pendu")
    print("6. Décodeur César")
    print("7. Gestionnaire de contact")
    print("**************************************")
    # Demande à l'utilisateur de faire un choix et retourne ce choix
    return input("Votre choix : ")

# Affichage initial du menu et récupération du choix de l'utilisateur
choix = affiche_menu()


# Boucle principale du programme
while choix != "0":
    # Utilisation de l'instruction match pour gérer les différents choix
    match (choix):
        case "1":
            # Calcul de remise
            montant = int(input('Montant : '))
            remise = int(input('La remise : '))
            calcul_remise(montant, remise)
        case "2":
            # Jeu de dés
            jeu_de_des()
        case "3":
            # Jeu du juste prix
            juste_prix()
        case "4":
            # Horloge numérique
            horloge()
        case "5":
            # Jeu du pendu
            pendu()
        case "6":
            # Décodeur César
            cesar()
        case "7":
            # Gestionnaire de contact
            contact()
    
    # Réaffichage du menu après chaque action
    choix = affiche_menu()

# Message de fin de programme
print("*** FIN DU PROGRAMME ***")
