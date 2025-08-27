#----------DICTIONNAIRE----------
bibliotheque = {
    "Warzone": {"nom": "Warzone", "prix": "GRATUIT", "taille": 95.},
    "Minecraft": {"nom": "Minecraft", "prix": 29.99, "taille": 24.},
    "R6X": {"nom": "R6X", "prix": "GRATUIT", "taille": 65.},
    "Roblox": {"nom": "Roblox", "prix": "GRATUIT", "taille": 95.},
    "GTA": {"nom": "GTA", "prix": 44.99, "taille": 103.}
}

boutique = {
    "Peak": {"nom": "Peak", "prix": "GRATUIT", "taille": 95},
    "Dead by Daylight": {"nom": "Dead by Daylight", "prix": 19.99, "taille": 50},
    "Red Dead Redemption 2": {"nom": "Red Dead Redemption 2", "prix": 14.99, "taille": 150},
    "CyberPunk 2077": {"nom": "CyberPunk 2077", "prix": 59.99, "taille": 70},
    "Call Of Duty : Black Ops 6": {"nom": "Call Of Duty : Black Ops 6", "prix": 69.99, "taille": 200}
}

stockage = 235
porte_monnaie = 100.00

#------------FONCTIONS------------
def afficher_jeux(biblio):
    print("Voici la liste des jeux possédés :")
    for i, jeu in enumerate(biblio):
        print(f"{i+1} - {jeu}")

def afficher_boutique():
    print("Jeux disponibles à l'achat :")
    for nom, infos in boutique.items():
        print(f"{nom} | Prix : {infos['prix']}€ | Taille : {infos['taille']}Go")

def acheter_jeu():
    global stockage, porte_monnaie
    afficher_boutique()
    nom_jeu = input("Nom du jeu à acheter : ")
    if nom_jeu in boutique:
        jeu = boutique[nom_jeu]
        prix = jeu['prix']
        taille = jeu['taille']
        if prix != "GRATUIT" and porte_monnaie < prix:
            print("Fonds insuffisants.")
            return
        if stockage < taille:
            print("Pas assez de stockage.")
            return
        if nom_jeu in bibliotheque:
            print("Jeu déjà possédé.")
            return
        bibliotheque[nom_jeu] = jeu
        if prix != "GRATUIT":
            porte_monnaie -= prix
        stockage -= taille
        print(f"{nom_jeu} ajouté à la bibliothèque !")
    else:
        print("Jeu non trouvé dans la boutique.")

def supprimer_jeu():
    global stockage
    afficher_jeux(bibliotheque)
    nom_jeu = input("Nom du jeu à supprimer : ")
    if nom_jeu in bibliotheque:
        taille = bibliotheque[nom_jeu]['taille']
        del bibliotheque[nom_jeu]
        stockage += taille
        print(f"{nom_jeu} supprimé de la bibliothèque.")
    else:
        print("Jeu non trouvé.")

def rechercher_jeu():
    nom_jeu = input("Nom du jeu à rechercher : ")
    if nom_jeu in bibliotheque:
        print(f"{nom_jeu} est dans votre bibliothèque.")
    else:
        print(f"{nom_jeu} n'est pas dans votre bibliothèque.")

def afficher_portemonnaie():
    print(f"Porte-monnaie : {porte_monnaie:.2f}€")
    print(f"Stockage restant : {stockage} Go")

def menu_steam():
    while True:
        print("\n=======================\n --* MENU STEAM *--\n=======================")
        print("1. Afficher les jeux possédés")
        print("2. Acheter un jeu dans la boutique")
        print("3. Supprimer un jeu de la bibliothèque")
        print("4. Rechercher un jeu dans la bibliothèque")
        print("5. Afficher le porte-monnaie et stockage")
        print("6. Quitter STEAM")
        try:
            choix = int(input("Votre choix = "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if choix == 1:
            afficher_jeux(bibliotheque)
        elif choix == 2:
            acheter_jeu()
        elif choix == 3:
            supprimer_jeu()
        elif choix == 4:
            rechercher_jeu()
        elif choix == 5:
            afficher_portemonnaie()
        elif choix == 6:
            print("A la prochaine !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

#---STEAM---
menu_steam()