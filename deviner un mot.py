nb_vie=7
mot_mystere='rayane'
mot_trouver='_'*len(mot_mystere)

while nb_vie >= 0 and mot_mystere!=mot_trouver :
   x=input("donner la lettre pour savoir si il est dans le mot : ")
   if x in mot_mystere:
      for i in range(len(mot_mystere)):
          
          if mot_mystere[i]==x :
             mot_trouver=mot_trouver[:i] + x + mot_trouver[i+1:]
             print(mot_trouver)
             print('vous avez juste:', nb_vie)
#si le nombre est faut              
   else:
       nb_vie-=1
       print('la lettre est fausse reesseyer')
       print('vous avez juste:', nb_vie)

   if mot_trouver==mot_mystere:
       print('bravo le mot était:',mot_mystere)
       
   elif nb_vie==0:
    print('vous avez perdue')
   
     
       
     