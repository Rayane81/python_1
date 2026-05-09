import random
choisir=['pierre','papier','ciseaux']
score_ordinateur=0
votre_score=0
rejouer="oui"
choix=["oui","non"]


print("       _bienvenue au jeu pierre papier ciseaux_     ")
print("")

while rejouer=="oui" :   
 votre_choix=input("choisissez entre pierre papier ciseaux :" )

 while votre_choix not in choisir :
    print("s'il vous plait choisissez entre pierre papier ciseaux seulement ")
    votre_choix =input("choisissez entre pierre papier ciseaux :" )

 choix_ordinateur=random.choice(choisir)
 print("alors l'ordinateur a choisi : ",choix_ordinateur)

 if choix_ordinateur==votre_choix :
    print("égalité!" )
    print("votre score est :",votre_score,"et le score de,l'ordinateur est :",score_ordinateur)

 elif(
    (votre_choix=="pierre" and choix_ordinateur=="ciseaux")or
    (votre_choix=="papier" and choix_ordinateur=="pierre")or
    (votre_choix=="ciseaux" and choix_ordinateur=="papier")
    ):
    votre_score+=1
    print("")
    print("bravo vous avez gagné !continuer jusqu'a atteindre le score ")
    print("votre score est :",votre_score)
 else :
    score_ordinateur+=1
    print("")
    print("vous avez perdue reéssayez encour une fois")
    print("le score de l'ordinateur est :",score_ordinateur)

 rejouer=input("voulez-vous rejouer ? (oui\non) :")
 while rejouer not in choix :
     print("vous dites oui ou non ")
     rejouer=input("voulez-vous rejouer ? (oui\non) :")
     
 print("merci d'avoir jouer a la prouchain !")
 break

