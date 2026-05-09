import random
nombre_secret=random.randint(1,100)
essai=0
nombre=0

print('        _bienvenue dans le jeu de devinette_         ')
print("")

print("_alors j'ai bien choisi un nombre entre 1 et 100 a toi de deviner !")
print("")

while nombre!=nombre_secret :
    nombre=int(input("donner votre premier nombre :"))
    if nombre<nombre_secret:
        essai+=1
        print("le nombre que vous avez deviner est petit")
    elif nombre > nombre_secret :
        essai+=1
        print("le nombre que vous avez choisi est grand")
        
if essai==0:
    print("magnifique vous avez trouver le nombre secret avec juste un essaye")
else:
 print("bravo vous avez trouver le nombre secret apres",essai,"fois essaye")
    