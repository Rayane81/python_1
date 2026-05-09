produit=[]
quantites=[]
while True:
 print("          Bien venue dans le Menu du stock           ")
 print("")
 print("1.ajouter un produit ")
 print("2.afficher le stock ")
 print("3.modifier une quantité")
 print("4.supprimer un produit ")
 print("5.modifier le nom de le produit ")
 print("0.quitter")

 choix=input("choisissez ce que vous voulez : ")
 if choix=="1":
     rep=True
     while rep!="non": 
       nom=input("donner le nom du produit : ")
       qet=int(input("donner aussi ca quantité : "))
       produit.append(nom)
       quantites.append(qet)
       print("le produit" ,nom, "est ajouté avec une qauntité de " ,qet)
       rep=input("vous voulez ajouter un autre produit : ")
     print(produit)
    
    
 elif choix=="2":
     if len(produit)==0:
        print("le stock est vide")
     else:
        print("les stock sont : ")
        for i in range(len(produit)):
            print(i+1,produit[i],"avec une quantité de : ",quantites[i])
 elif choix=="3":
    num=int(input("donner le num du produit pour changer ca quantité : "))
    if 1<=num<=len(produit):
      nouvelle_qnt=input("dans la nouvelle quantité : ")
      quantites[num-1]=nouvelle_qnt 
      print("le nom du produit est bien devenue ",nouvelle_qnt)
    else:
        print("le produit n'existe pas")
 elif choix=="4":
    num=int(input("donner le num du produit que vous voulez supprimer : "))
    if 1<=num<=len(produit):
        produit.pop(num-1)
        quantites.pop(num-1)
        print("le produit",nom,"est supprimer")
    else:
        print("le produit n'existe pas") 
 elif choix=="5":
    num=int(input("donner le num de le produit : "))
    if 1<=num<=len(produit):
        nouveau_nom=input("donner le nouveu nom que vous voulez : ")
        produit[num-1]=nouveau_nom
        print("le nom est bien devenu ",nouveau_nom)
    else:
        print("le produit n'existe pas")
 elif choix=="0":
     
    print("bonne journeé")
    break
else :
     print("choix invalide")
    
