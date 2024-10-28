// Données de base
let typeVehicule = "Voiture";  // Peut être "Voiture", "Moto" ou "Camion"
let ageVehicule = 6;           // Âge du véhicule en années
let kilometrageAnnuel = 25000; // Kilométrage annuel
let prime = 0;

// Définition de la prime de base selon le type de véhicule
if (typeVehicule === "Voiture") {
    prime = 500;
} else if (typeVehicule === "Moto") {
    prime = 300;
} else if (typeVehicule === "Camion") {
    prime = 1000;
}

// Majoration pour l'âge du véhicule
if (ageVehicule > 5) {
    prime *= 1.10;  // +10%
}

// Majoration pour le kilométrage annuel
if (kilometrageAnnuel > 30000) {
    prime *= 1.15;  // +15%
} else if (kilometrageAnnuel > 20000) {
    prime *= 1.05;  // +5%
}

console.log("Prime d'assurance :", prime);
