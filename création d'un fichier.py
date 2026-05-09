import os 
class filemanager:
    
    def __init__(self):
        pass
    
    def menu(self):
         print("          la gestion de fichier           ")
         print("1.liste des fichier d'un dossier")
         print("2.crée un fichier")
         print("3.lire un fichier ")
         print("4.écrire dans un fichier ")
         print("5.supprimer un fichier")
         print("6.renommer un fichier")
         print("0.quitter ")
    
    def liste_fichiers (self):
         
         chemin=input("chemin du dossier : ")
         
         if not os.path.exists(chemin):
             print("le dossier n'existe pas ")
             return 
         fichiers=os.listdir(chemin)
         if len(fichiers)==0:
                print("dossier vide")
         else :
                print("fichiers : ")
                for f in fichiers:
                    print("_",f)
        
    def cree_fichier(self):
        rep=True
        while rep!="non":
        
         nom=input("donner le nom de fichier : ")
         try:
            with open(nom,"x"):
                print("le fichier est crée ")
                rep=input("vous voulez rajouter un autre fichier")
                print(nom)
         except :
            print("le fichier existe déjà")
                    
    def lire_fichier(slef):
        
        nom=input("le nom du fichier à lire : ")
        try:
            with open(nom,"r")as f:
                contenu=f.read()
                print("le contenu du fichier",contenu)
        except:
            print("le fichier n'existe pas")
    
    def ecrire_fichier(self):
        nom=input("le nom du fichier :")
        texte=input("texte à ajouter: ")
        try:
            with open(nom,"a") as f:
                f.write(texte)
                print("texte ajouter")
        except:
            print("erreur lors de la lecture")
        
    def supprimer_fichier(self):
        nom=input("le nom du fichier a supprimer : ")
        if os.path.exists(nom):
            os.remove(nom)
            print("fichier supprimer")
        else:
            print("le fichier n'existe pas")
            
    def renommer_fichier(sefl):
        ancien=input("donner le ancien nom : ")
        nouveau=input("donner le nouveu nom: ")
        
        if os.path.exists(ancien):
            os.rename(ancien,nouveau)
            print("fichier est renommer")
        else:
            print("fichier introuvable")
        
    def run(self):
        repe=True
        while repe!="non":
            self.menu()
            choix=int(input("votre choix : "))
        
            
            if choix==1:
                self.liste_fichiers()
            elif choix==2:
                self.cree_fichier()
            elif choix==3:
                self.lire_fichier()
            elif choix==4:
                self.ecrire_fichier()
            elif choix==5:
                self.supprimer_fichier()
            elif choix==6:
                self.renommer_fichier()
        repe=input("vous voulez rajoujet quelque chose")
        if choix==0:
             print("au revoir")
          
        else :
                print("choix invalide choisissez entre 0 et 6 sinon je vais pleure")
                

manager=filemanager()
manager.run()

    
        
        
        
        
        
        
        
                    
                    
                    
                    
                    
                    
                    
                
             
        
        
    