class tache :
    def __init__(self,nom,terminee):
        self.nom=nom
        self.terminee=False
        
taches=[]
nb_tache=int(input("combien de tache voulez vous créer? "))

for i in range(nb_tache):
    nom=input(f"donne le nom de la {i+1} tache: ")
    rep=input("la tache est-elle terminer ou pas ?").lower()
    if rep=="oui":
        terminee=True
    else:
        terminee=False
    tachee=tache(nom,terminee)
    taches.append(tachee)
print("")       
print("                   les listes qui sont disponibles actluellement sont :                     ")

for i,tache in enumerate(taches):
    print(f"{i+1}.",nom,"->",terminee)
    
    
print("voulez vous :")
print("1_ajouter une taches")
print("2_marquer une tache comme termineé")
print("3_supprimer une tache")
print("4_quitter")

choix=int(input("choissez entre ces 4 propositions : "))
if choix==1:
    nom=input(f"donne le nom de la {i+1} tache: ")
    rep=input("la tache est-elle terminer ou pas ?").lower()
    if rep=="oui":
        terminee=True
    else:
        terminee=False
    tachee=tache(nom,terminee)
    taches.append(tache)
    print("tache ajoutter avec succés")
    
elif choix==2:
    num=int(input("numero de la tache a marquer comme terminee : "))
    if 1<=num<=len(taches):
        if taches[num-1].terminee==True:
            print("la tache", num ,"est deja teminee")
        else:
          taches[num-1].terminee=True 
          print("apres la confirmation la tache",num, "est marquer comme terminer")
    else :
        print("le num de cette tache n'hexsite pas")

elif choix==3:
     num=int(input("numero de la tache",num," est supprimer"))
     if 1<=num<=len(taches):
        taches.pop(num-1)
        print("apres la confirmation la tache est supprimer")
     else :
        print("le num de cette tache n'hexsite pas")
        
elif choix==4:
    print("au revoir")
    

        
        
        
    
    
        
    
    

    
    
    
    