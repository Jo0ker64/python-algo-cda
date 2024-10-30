# # Importation des modules nécessaires
# from threading import Timer  # Pour programmer des actions à intervalles réguliers
# from datetime import datetime  # Pour obtenir et formater la date et l'heure

# class Clock:
#     def __init__(self):
#         # Initialisation des attributs de la classe
#         self.is_alive = False  # Indique si l'horloge est en marche
#         self.timer = None  # Stocke l'objet Timer pour les mises à jour

#     def start(self):
#         """Démarre l'horloge"""
#         self.is_alive = True  # Marque l'horloge comme active
#         self.__set_time()  # Commence l'affichage de l'heure
#         print("L'horloge est démarrée. Tapez 'exit' pour arrêter.")

#     def stop(self):
#         """Arrête l'horloge"""
#         self.is_alive = False  # Marque l'horloge comme inactive
#         if self.timer:
#             self.timer.cancel()  # Annule le timer s'il existe
#         print("\nL'horloge est arrêtée.")

#     def __set_time(self):
#         """Affiche l'heure et programme la prochaine mise à jour"""
#         if not self.is_alive:
#             return  # Sort de la fonction si l'horloge n'est pas active

#         # Obtient et formate l'heure GMT et locale
#         gmt = datetime.utcnow().strftime('%A %d %B %Y, %H:%M:%S')
#         lcl = datetime.now().strftime('%A %d %B %Y, %H:%M:%S')
        
#         # Affiche les heures GMT et locale
#         print(f"GMT:    {gmt}")
#         print(f"Locale: {lcl}")

#         # Programme la prochaine mise à jour dans 1 seconde
#         self.timer = Timer(1, self.__set_time)
#         self.timer.start()

# def main():
#     clock = Clock()  # Crée une instance de la classe Clock
#     try:
#         clock.start()  # Démarre l'horloge
        
#         while True:
#             # Demande à l'utilisateur s'il veut quitter
#             command = input("Entrez 'exit' pour quitter : ").strip().lower()
#             if command == 'exit':
#                 clock.stop()  # Arrête l'horloge si l'utilisateur tape 'exit'
#                 break  # Sort de la boucle
            
#     except KeyboardInterrupt:
#         # Gère l'interruption par Ctrl+C
#         clock.stop()  # Arrête l'horloge proprement

# # Point d'entrée du script
# if __name__ == '__main__':
#     main()  # Appelle la fonction principale
print("Lancement de l'horloge numérique ...")
import time
from datetime import datetime, timedelta

def horloge():
    # Obtenez l'heure actuelle au lancement du script
    heure_initiale = datetime.now()
    print("Heure de départ:", heure_initiale.strftime("%H:%M:%S"))

    # Durée pour l'affichage de l'horloge (en secondes)
    duree_affichage = 10  # exemple : 10 secondes

    while True:
        heure_actuelle = datetime.now()
        temps_ecoule = (heure_actuelle - heure_initiale).total_seconds()
        
        # Afficher l'heure qui défile sans mise à jour en temps réel
        heure_defilante = (heure_initiale + timedelta(seconds=temps_ecoule)).strftime("%H:%M:%S")
        print("Heure actuelle:", heure_defilante)
        
        if temps_ecoule >= duree_affichage:
            print("Fin de l'horloge.")
            break
        
        # Pause pour ne pas réactualiser en continu
        time.sleep(1)

# Exécute l'horloge
horloge()