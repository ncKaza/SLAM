prenom = input ("Quel est ton prenom ?")
print ("tu t'apelle",prenom,)
age = int (input ("ton age?"))
print ("votre age est",age,"ans")
print("Bonjour",prenom,"!")
if age >= 18:
    print ("tu es majeur.")
else:
    print ("tu es mineur")
age_dans_15_ans = age + 15
print ("Dans 15 ans tu auras,",age_dans_15_ans,"ans")