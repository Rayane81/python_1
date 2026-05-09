
class Matiere:
    def __init__(self, nom, coefficient):
        self.nom = nom
        self.coefficient = coefficient
        self.notes = []
        
    def notes_ajouter(self):
       while True :
           note_str=input(f"donner la note pour {self.nom}(ou stop pour terminer)")
           if note_str.lower()=="stop":
               break
           while True:
            try:
               note=float(note)
               if 0<=note<=20:
                   self.notes.append(note)
                   break
               else:
                   note_str=input("la note doit etre ente 0 et 20")
            except:
               print("entrer un nombre valide")
                   
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.matieres = []

    def ajouter_matiere(self, nom_matiere, coefficient, note):
        mat = Matiere(nom_matiere, coefficient)
        mat.notes.append(note)
        self.matieres.append(mat)

    def calculer_moyenne(self):
        total = 0
        total_coef = 0
        for m in self.matieres:
            if len(m.notes)==0:
                continue
            moyenne_matiere = sum(m.notes)/len(m.notes)
            total += moyenne_matiere * m.coefficient
            total_coef += m.coefficient
        if total_coef == 0:
            return 0
        return total / total_coef

    def afficher_bulletin(self):
        print(f"\nBulletin de {self.nom}")
        for m in self.matieres:
            print(f"{m.nom} (coef {m.coefficient}) : notes {m.notes}")
        print("Moyenne générale :", round(self.calculer_moyenne(),2))


#Programme principal
nom_etudiant = input("Nom de l'étudiant : ")
etudiant = Etudiant(nom_etudiant)

while True:
    nom_matiere = input("\nNom de la matière (ou 'stop' pour terminer) : ")
    if nom_matiere.lower() == "stop":
        break
    coef = int(input("Coefficient de la matière : "))
    note = float(input("Première note de la matière : "))
    
    etudiant.ajouter_matiere(nom_matiere, coef, note)
etudiant.afficher_bulletin()