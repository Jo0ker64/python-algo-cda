# Catégorie d'assurance pour un véhicule
# Ecrire un script qui retourne la catégorie d’un assuré en fonction des critères
# suivants
# Critères :
# Catégorie "Rouge" : Moins de 2 ans de permis ou plus de 3 accidents.
# Catégorie "Orange" : Moins de 5 ans de permis et entre 1 et 2
# accidents.
# Catégorie "Vert" : Plus de 5 ans de permis, avec moins de 1 accident.
# Catégorie "Bleu" : Plus de 10 ans de permis sans accident.

def obtenir_nombre_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Obtention des informations de l'assuré
annees_permis = obtenir_nombre_entier("Depuis combien d'années avez-vous votre permis ? ")
nombre_accidents = obtenir_nombre_entier("Combien d'accidents avez-vous eu ? ")

# Détermination de la catégorie
if annees_permis < 2 or nombre_accidents > 3:
    categorie = "Rouge"
elif annees_permis < 5 and 1 <= nombre_accidents <= 2:
    categorie = "Orange"
elif annees_permis >= 5 and nombre_accidents < 1:
    categorie = "Vert"
elif annees_permis > 10 and nombre_accidents == 0:
    categorie = "Bleu"
else:
    categorie = "Non catégorisé"

# Affichage du résultat
print(f"\nRésultat de l'évaluation :")
print(f"Années de permis : {annees_permis}")
print(f"Nombre d'accidents : {nombre_accidents}")
print(f"Catégorie d'assurance : {categorie}")

# Explication de la catégorie
if categorie == "Rouge":
    print("Explication : Catégorie à haut risque. Moins de 2 ans de permis ou plus de 3 accidents.")
elif categorie == "Orange":
    print("Explication : Catégorie à risque modéré. Moins de 5 ans de permis et entre 1 et 2 accidents.")
elif categorie == "Vert":
    print("Explication : Catégorie à faible risque. Plus de 5 ans de permis, avec moins de 1 accident.")
elif categorie == "Bleu":
    print("Explication : Catégorie à très faible risque. Plus de 10 ans de permis sans accident.")
else:
    print("Explication : Votre profil ne correspond à aucune catégorie prédéfinie.")
