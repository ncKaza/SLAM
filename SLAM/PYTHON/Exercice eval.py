#les fonctions
def afficher_liste(liste):
    print("Voici la liste : ")
    for i, eleve in enumerate(liste):
        print(f"{i} - {eleve}")

def ajout_liste(liste):
    print("Voici la liste avant modification : ")
    afficher_liste(liste)
    new_prenom = (input("Saisissez le prenom de l'élève à rajouter : "))
    liste.append(new_prenom)
    print(f"Voici la liste après modification{liste}")
    menu(liste)
    
def supp_liste(liste):
    while True:
        print("Voici la liste avant modification ")
        afficher_liste(liste)
        try:
           eleve_supp = int(input("Saisissez l'indice de l'eleve que vous souhaitez supprimer : "))
        except ValueError:
            print("Saisissez un indice valide")
            return supp_liste(liste)
        if eleve_supp < 0 or eleve_supp >= len(liste) :
            print("Saisissez un indice valide") 
            return supp_liste(liste)        
        else:
            liste.pop(eleve_supp)
            print("Voici la liste apres modification :")
            afficher_liste(liste)
        menu(liste)

def rechercher_liste(liste):
    recherche_eleve = input("Saisissez le nom de l'eleve que vous cherchez : ")
    if recherche_eleve in liste :
        print("L'eleve est présent dans la liste")
    else :
        print("l'eleve n'est pas présent dans la liste")
    menu(liste)

def modifier_liste(liste):
    print("Voici la liste :")
    afficher_liste(liste)
    try :
        indice_eleve = int(input("Saisissez l'indice de l'eleve dont vous souhaitez changer le nom : "))
    except ValueError:
        print("Saisissez un nombre valide")
        return modifier_liste(liste)
    new_nom_eleve = input("Saisissez le nouveau de l'eleve : ")
    liste[indice_eleve] = new_nom_eleve
    print("liste apres modif :")
    afficher_liste(liste)

def menu(liste):
    while True :
        print("----------------------------------\n         MENU PRINCIPALE \n----------------------------------")
        print("1- Afficher les eleves")
        print("2- Ajouter un eleve")
        print("3- Supprimer un eleve")
        print("4- Rechercher un eleve")
        print("5- Modifier un eleve")
        print("6- Quitter le programme")
        try :
            choix = int(input("Saisissez votre choix : "))
        except ValueError:
            print("Saisissez un nombre valide")
            continue
        if choix == 1 :
            afficher_liste(liste)
        elif choix == 2 :
            ajout_liste(liste)
        elif choix == 3:
            supp_liste(liste)
        elif choix == 4:
            rechercher_liste(liste)
        elif choix == 5:
            modifier_liste(liste)
        elif choix == 6:
            print("Merci a bientot ! ")
            break

        


#code principal
liste = [ "Weymin","Alexis","Mickael","Elodie","Wasso","Allan","Josyas"]
menu(liste)