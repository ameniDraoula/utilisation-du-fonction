#on va utiliser une fonction et on va l'appeler par la suite 
def demander_age():
    age=0
    while age== 0 :
        age_str=input ("quel est votre age ?")
            # input retoune tjr une chaine de carctére
        try:
            age=int(age_str) 
            # on converti le resultat en entier avec int()
        except:
            # gestion d'une exception
            print("erreur !! vous devez rentrer un nombre pour l'age")
    return age

# demander le nom
nom=""
while nom== "":
    nom= input("quel est votre nom ?")
# demander l'age
age=demander_age()
# afficher le resultat 
print( "vous vous appelez"+nom +", vous avez " + str(age)+ " ans .")
print("l'an prochain  vous aurez "+ str(age+1)+" ans")
