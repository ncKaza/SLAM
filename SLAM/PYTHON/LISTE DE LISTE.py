#----------DICTIONNAIRE----------
bibliotheque = {
    "Warzone":
      {"nom" : "Warzone", "prix" : "GRATUIT", "taille" : 95.},
    "Minecraft":
      {"nom" : "Minecraft", "prix" : 29.99, "taille" : 24.},
    "R6X":
      {"nom" : "R6X", "prix" : "GRATUIT", "taille" : 65.},
    "Roblox":
      {"nom" : "Roblox", "prix" : "GRATUIT", "taille" : 95.},
    "GTA":
      {"nom" : "GTA", "prix" : 44.99, "taille" : 103.}
}

boutique = {
    "Peak":
      {"nom" : "Peak", "prix" : "GRATUIT", "taille" : 95},
    "Dead by Daylight":
      {"nom" : "Dead by Daylight", "prix" : 19.99, "taille" : 50},
    "Red Dead Redemption 2":
      {"nom" : "Red Dead Redemption 2", "prix" : 14.99, "taille" : 150},
    "CyberPunk 2077":
      {"nom" : "CyberPunk 2077", "prix" : 59.99, "taille" : 70},
    "Call Of Duty : Black Ops 6":
      {"nom" : "Call Of Duty : Black Ops 6", "prix" : 69.99, "taille" : 200}

}

stockage = 235
porte_monnaie = 100.00
#------------FONCTION------------
def afficher_jeux():
    print("Voici la liste des jeux :")
    for i, jeu in enumerate(jeux):
        print(f"{i} - {jeu}")

def achat_jeux (jeux,):
    print(f"Votre bibliotheque actuelle : ")
    afficher_jeux(jeux)
    print("Voici la liste des jeux disponibles à l'achat : ")
    print(jeux_boutique[0])
    jeux_acher
    new_jeu = input("Saisissez le nom du jeux : ")
    jeux.append(new_jeu)
    print(f"Votre bibliotheque apres l'ajout du jeux :")
    afficher_jeux(jeux)

def menu_steam():
    while True:
        print("=======================\n --* MENU STEAM *--\n=======================")
        print("1. Afficher les jeux possédé")
        print("2. Acheté un jeu dans la boutique")
        print("3. Supprimer un jeux de la bibliotheque")
        print("4. Rechercher un jeu dans la bibliotheque")
        print("5. Afficher le porte-monnaie")
        print("6. Quitter STEAM")
        try:
            choix = int(input("Votre choix = "))
        except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue
        if choix == 1:
            afficher_jeux(jeux)
        elif choix == 2:
            ajout_liste(liste)
        elif choix == 3:
            supp_depuis_indice(liste)
        elif choix == 4:
            rechercher_depuis_nom(liste)
        elif choix == 5:
            modifier_depuis_indice(liste)
        elif choix == 6:
            print("A la prochaine ! ")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

#---STEAM---
bibliotheque