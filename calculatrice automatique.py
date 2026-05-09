print("          calculatrice         ")


print('choisissez quelle operation voulais vous effectuer :')
print("")
print('1.Addition')
print('2.Soustraction')
print('3.Multiplication')
print('4.Division')
print('5.Quitter')

choix=input("_l'operation num = ")
if choix in ['1','2','3','4','5']:
 if choix=="1":
    print("alors vous souhaitez faire l'addition entre ces nombre ")
    a=float(input("donenr votre premiere valeur :"))
    b=float(input("donenr votre deuxiéme valeur :"))
    print("le resultat :",a+b)
    
 elif choix=="2":
    print("alors vous souhaitez faire soustraction entre ces nombre ")
    a=float(input("donenr votre premiere valeur :"))
    b=float(input("donenr votre deuxiéme valeur :"))
    print("le resultat :",a-b)
    
 elif choix=="3":
    print("alors vous souhaitez faire multiplication entre ces nombre ")
    a=float(input("donenr votre premiere valeur :"))
    b=float(input("donenr votre deuxiéme valeur :"))
    print("le resultat :",a*b)
        
 elif choix=="4":
     print("alors vous souhaitez faire division entre ces nombre ")
     a=float(input("donenr votre premiere valeur :"))
     b=float(input("donenr votre deuxiéme valeur :"))
     if b!=0:
      print("le resultat :",a/b)
     else:
        print("erreur:on ne peut pas diviser sur 0")
 elif choix=="5":
    print("Au revoir ")

else :
 print("invalide choisissez jute entre 1..5")
    
    
    
    
    
    
    