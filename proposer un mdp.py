import random
import string

def generer_mot_de_passe(longueur):
    caracteres=string.ascii_letters+string.digits+string.punctuation
    mot_de_passe="".join(random.choice(caracteres)for i in range(longueur))
    
    return mot_de_passe


taille=int(input("quelle est la longueur souhaites_tu pour votre mots de passe : "))
if taille<5:
    print("votre mode de passe n'est pas vraiment securiser mais je te propose ce mots de passe : ")
    resultat=generer_mot_de_passe(taille)
    print("votre mot de passe est bien :",resultat)
    
else:
    resultat=generer_mot_de_passe(taille)
    print("votre mot de passe est bien :",resultat)
    

    