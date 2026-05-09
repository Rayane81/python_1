class comptebancaire :
    def __init__(self,nom,solde):
        self.nom=nom
        self.solde=solde
        
    def afficher(self):
        print("le nom du compte est :",self.nom,"et le solde est :",self.solde)

    def dispose(self,montant):
        self.solde+=montant
        print("la nouvelle somme apres avoir disposer",montant,"est bien : ",self.solde)
    
    def retirer(self,montant):
        if montant>self.solde:
            print("solde insuffisant, impossible de retirer")
        else:
            self.solde-=montant
            print("la somme apres retire",montant,"est :",self.solde)
        
nb_compte=int(input("combien de compte voulez vous créer : "))
comptes=[]

for i in range(nb_compte):
  nom=input(f"le nom du compte {i+1}: ")
  solde=int(input(f"le solde de compte num {i+1} :"))
  comptes.append(comptebancaire(nom,solde))
  
for i,comptebancaire in enumerate(comptes):
   comptebancaire.afficher()
   
   
print("______________voulez vous ______________ ")
print("1.rajoutter")
print("2.retirer")
print("3.quitter")
choix=int(input("vous voullez quoi rajoutter 1 , retirer 2 ,quitter 3 : "))

if choix==1 :
  num=int(input("numero de compte :"))  
  montant=int(input("donner la somme que vous voulez rajouter: "))
  comptes[num-1].dispose(montant)

elif choix==2:
  num=int(input("numero de compte :")) 
  montant_retirer=int(input("la somme a retirer :"))
  comptes[num-1].retirer(montant_retirer)
          
          
elif choix==3 :
    print("bonne journneé")