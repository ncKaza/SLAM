# Les fonctions
def ajout_liste (liste):
    print(f"Liste avant l'ajout du jeux : {liste}")
    new_jeu = input("Saisissez le nom du jeux : ")
    liste.append(new_jeu)
    print(f"Voici la liste apres l'ajout du jeux : {liste}")
    

def supp_depuis_indice (liste):
    print(f"Liste avant modification : {liste}")
    try:
        liste_supp = int(input("Saisissez l'emplacement du jeux que vous voulez supprimer (ex : 1) : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return supp_depuis_indice(liste)
    if liste_supp < 0 or liste_supp >= len(liste):
        print("Indice invalide. Veuillez réessayer.")
        return supp_depuis_indice(liste)
    else :
        liste.pop(liste_supp)
        print(f"Voici la liste apres modification {liste}")
    

def rechercher_depuis_nom (liste):
    nom = input("Saisissez le nom du jeux que vous recherchez : ")
    if nom in liste :
        print("Ce jeux est présent dans la liste")
    else:
        print("Ce jeux n'est pas présent dans la liste")
    
   
def modifier_depuis_indice (liste):
    print("Liste avant modification : ", liste)
    pos_rempl = int(input("Saisissez l'emplacement du jeux dont vous souhaitez changer le nom (ex : 1): "))
    if pos_rempl < 0 or pos_rempl >= len(liste):
        print("Indice invalide. Veuillez réessayer.")
        return modifier_depuis_indice(liste)
    nom_rempl = input("Saisissez le nouveau nom du jeux : ")
    liste[pos_rempl] = nom_rempl
    print("Liste après modification : ", liste)
    

def menu_liste(liste):
    while True:
        print("********************\n * MENU DES JEUX *\n********************")
        print("1. Afficher les jeux")
        print("2. Ajouter un jeux")
        print("3. Supprimer un jeux")
        print("4. Rechercher un jeux")
        print("5. Modifier le nom d'un jeux")
        print("6. Quitter le programme")
        try:
            choix = int(input("Votre choix = "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if choix == 1:
            print("Voici la liste des jeux :")
            print(liste)
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


# Le programme principal

liste = ["Warzone", "Minecraft", "R6", "Roblox" , "GTA"]

menu_liste(liste)