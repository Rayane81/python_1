class compte:
    def __init__(self,nom, solde):
        self.nom=nom
        self.solde=solde
    def afficher(self):
        print(f"le nom du compte est :{self.nom}:{self.sold}DA")
    def deposer(self, montant):
        self.solde+=montant
    def retirer(self,montant):
        if montant>self.solde:
            print("solde insuffisant!")
        else:
            self.solde-=montant

comptes=[]
while True :
    print("le menu:")
    print("1.créer un compte")
    print("2.afficher les comptes")
    print("3.Déposer de l'argent ")
    print("4.Retirer de l'argent")
    print("0.Quitter")

    choix=input("choisissez c que vous voulez: ")

    if choix=="1":
        nom=str(input("donner le nom du compte :"))
        solde=float(input(f"donner le solde que vous avez deja sur ce compte ou que vous vouler rajouter commme premier montant pour le compte{nom} :"))
        c=compte(nom, solde)
        comptes.append(c)
        print("le compte est créer!")

    elif choix=="2":
        if len(comptes)==0:
            print("aucun copmte enregister!")
        else:
            for c in comptes:
                c.afficher
            
    elif choix=="3":
        nom=input("donner le nom du compte que vous voulez retirer: ")
        trouver=False
        for c in comptes:
            if c.nom.lower()==nom.lower():
                montant=float(input("donner la somme que vous voulez rajoutter:"))
                c.deposer(montant)
                print("Dépot effectué!")
                trouver=True
                break
        if not trouver:
            print("compte introuvable!")

    elif choix=="4":
        nom=input("donner le nom de compte que vous voulez retirer")
        trouver=False
        for c in comptes:
            if c.nom.lower()==nom.lower():
                montant=float(input("donner la somme que vous voulez retirer:"))
                c.retirer(montant)
                trouver=True
                break
        if not trouver:
            print("compte introuvable!")

    elif choix=="0":
        print("Fermiture")
        break

    else:
        print("choix invalide!")






