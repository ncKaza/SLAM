#Exo 1.2
"""
note1 = float (input ("inserez la premiere note "))
note2 = float (input ("inserez la deuxieme note "))
note3 = float (input ("inserez la troisieme note "))
moyenne = (note1 + note2 + note3 ) / 3
print (f"La moyenne des trois notes est {moyenne}")
"""

#Exo 1.3
"""
valeur1 = input ("inserez la premiere valeur ")
valeur2 = input ("inserez la deuxieme valeur ")
valeur3 = valeur1
valeur1 = valeur2
valeur2 = valeur3
print (valeur1)
print (valeur2)
"""


"""
#Exo 1.5
porte_monnaie = 10000
montant_produit_acheter = int(input ("Insérez le montant du produit acheté:") )
porte_monnaie = porte_monnaie - montant_produit_acheter
if montant_produit_acheter > 10000 :
    print ("Vous n'avez pas assez d'argent pour acheter ce produit")
else :
 
 print (f"Après achat du produit le montant du porte monnaie est de{porte_monnaie} ")
"""

"""
#Exo 1.6
def calcul_imc(masse, taille):
    return masse/(taille**2)
 
masse_utilisateur = int(input("Entrez votre poids en kg:"))
taille_utilisateur = float(input("Entrez votre taille en m"))
imc = calcul_imc(masse_utilisateur, taille_utilisateur)
 
if imc >= 25.0:
    print("Vous êtes en surpoids.")
elif imc < 18.5:
    print("Vous êtes maigre.")
else:  
    print("Vous avez une corpulence normale.")
"""
"""
#2.1
import time 
nombre = int(input ("Insérez un nombre positif: "))
if nombre < 0 :
    print ("Ce n'est pas un nombre positif")
else:
    for i in range (nombre, -1, -1 ):
        print (i)
        time.sleep(1)

""""""
#Exercice 2.2 - table de multiplication
#Demander à l'utilisateur un nombre entre 1 et 9
#Le programme doit afficher la table de multiplication de ce nombre
nombre = int(input ("Insérez un chiffre entre 1 et 9 : "))
if nombre <= 0:
    print ("Ce n'est pas un chiffre entre 1 et 9")
elif nombre > 9:
    print ("Ce n'est pas un chiffre entre 1 et 9")
else: 
    for i in range (1, 11):
        print (f"{nombre} x {i} = {nombre * i}")
""""""
#Exercice 2.3 - moyenne d'un nombre de notes déterminé
#Demander à l'utilisateur combien de notes il souhaite saisir
#Lui demander ensuite de saisir les notes correspondantes
#Le programme doit calculer la moyenne de ces notes

nombre_notes = int(input("Combien de notes souhaitez-vous saisir ? "))
if nombre_notes <= 0:
    print("Le nombre de notes doit être supérieur à 0.")   
else:
    somme_notes = 0
    for i in range(nombre_notes):
        note = float(input(f"Entrez la note {i + 1} : "))
        somme_notes += note
    moyenne = somme_notes / nombre_notes
    print(f"La moyenne des {nombre_notes} notes est {moyenne:.2f}")
""""""
#Exercice 2.4 - moyenne d'un nombre de notes indéterminé
#Faire saisir les notes jusqu'à ce que l'utilisateur saisisse 0
#Le programme doit calculer la moyenne des notes saisies (0 non compris. il sert juste pour signaler que la saisie est terminée)
somme_notes = 0
nombre_notes = 0
while True:
    note = float(input("Entrez une note (0 pour terminer) : "))
    if note == 0:
        break
    somme_notes += note
    nombre_notes += 1
if nombre_notes > 0:
    moyenne = somme_notes / nombre_notes
    print(f"La moyenne des {nombre_notes} notes est {moyenne:.2f}")
else:
    print("Aucune note n'a été saisie.")
""""""
#Exercice 2.5 - mot inversé
#Demander à l'utilisateur un mot.
#Afficher ce mot à l'envers, lettre par lettre.
mot = input("Entrez un mot : ")
mot_inverse = mot[::-1]
for lettre in mot_inverse:
    print(lettre, end=' ')
print()  # Pour ajouter une nouvelle ligne après l'affichage du mot inversé 
""""""

#Exercice 1 (Madame) demander un bn de notes -> liste ->Calcul moyenne
nombre_notes = int(input("Combien de notes souhaitez-vous saisir ? "))
if nombre_notes <= 0:
    print("Le nombre de notes doit être supérieur à 0.")
else :
    notes = []
    for i in range(nombre_notes):
        note = float(input(f"Entrez la note {i + 1} : "))
        notes.append(note)
    moyenne = sum(notes) / nombre_notes
    print(f"La moyenne des {nombre_notes} notes est {moyenne:.2f}")
""""""
#Exercice 2.6 - juste prix
import random
nb_aleatoire = random.randint(1, 100)
tentatives = 1  # On compte la première tentative
nb_utilisateur = int(input("Devinez le nombre entre 1 et 100 : "))
while nb_utilisateur != nb_aleatoire:  
    if nb_utilisateur < nb_aleatoire:
        print("C'est plus grand !")
    else:
        print("C'est plus petit !")
    nb_utilisateur = int(input("Essayez à nouveau : "))
    tentatives += 1  # On incrémente à chaque essai
print(f"Bravo ! Vous avez trouvé le nombre en {tentatives} tentatives.")
""""""
#Exercice 3.1 - liste de fruits, Demander à l'utilisateur de saisir 5 fruits différents, Créer une liste avec ces fruits et l'afficher
fruits = []
for i in range(5):
    fruit = input(f"Entrez le fruit {i + 1} : ")
    fruits.append(fruit)
print("Liste des fruits :", fruits)
""""""
#Exercice 3.2
animaux = ["chien", "chat", "poisson", "cheval"]
utilisateur_animal_ = input("Saisissez un animal : ")
if utilisateur_animal_ in animaux:
    print(f"L'animal {utilisateur_animal_} est dans la liste.")
else :
    print("L'animal n'est pas dans la liste.")
""""""
#Exercice 3.3
pays = ["Nouvelle-Calédonie", "Fidji", "Vanuatu", "Australie"]
pays_a_supp = input("Entrez le nom du pays à supprimer : ")
if pays_a_supp in pays:
    pays.remove(pays_a_supp)
    print(f"Le pays {pays_a_supp} a été supprimé de la liste.")
else:
    print("Le pays n'est pas dans la liste.")
"""""""
#Exercice 3.4
is_running = True
prenoms = []
while is_running:
    saisie=input("saisissez plusieurs prénoms(STOP pour fin de saisie) :").strip()
    if "STOP" in prenoms :
       is_running = False
    else:
        prenoms
print(prenoms)
""""""
# Exercice 3.4 - Trier les prénoms CORRECTION

# Initialisation de la liste
prenoms = []

# Saisie des prénoms
while True:
    saisie = input("Entrez un prénom (ou STOP pour terminer) : ").strip()
    if saisie.upper() == "STOP":
        break
    elif saisie:
        prenoms.append(saisie)
    else:
        print("La saisie ne peut pas être vide.")

# Tri de la liste en ordre alphabétique (non sensible à la casse)
prenoms_triees = sorted(prenoms, key=lambda x: x.lower())

# Affichage du résultat
print("\nListe des prénoms triés :")
for prenom in prenoms_triees:
    print("-", prenom)
""""""
 

#Exercice1 15/07 13h25

notes = []

for i in range(3) :
    valeur = int(input(f"Saisissez la note {i+1} : "))
    notes.append(valeur)

moyenne = 0
for n in notes:
    moyenne += n

moyenne = moyenne /3

print(f"La moyenne des notes est : {moyenne}")
""""""
#Exercice2 15/07 13h25
nbr_notes = int(input("Combien de notes voulez vous saisir ?"))
notes = []

for i in range(nbr_notes) :
    valeur = float(input(f"Saisissez la note {i+1} : "))
    notes.append(valeur)

moyenne = 0
for n in notes:
    moyenne += n

moyenne = moyenne / nbr_notes
moy_arrondi = round(moyenne, 2)
print(f"La moyenne des notes est : {moy_arrondi}")
"""
def afficher_bonjour(prenom, age):
    print("Bonjour ")

def renvoyer_age_majorite(age):
    age = 18
    return ag
#Prog principale
