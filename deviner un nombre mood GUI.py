import tkinter as tk
import random
nombre_secret=random.randint(1,100)

fenetre = tk.Tk()
fenetre.title("jeu de devinette!")
fenetre.geometry("300x200")

label_titre=tk.Label(fenetre,text="jeu de devinette",font=("Arial",16))
label_titre.pack(pady=10)

label_info=tk.Label(fenetre,text="bonjour,alors le jeu est simple j'ai choisi un nomnre entre 1 et 100 a toi de deviner ce nombre")
label_info.pack()
entree=tk.Entry(fenetre)
entree.pack(pady=5)

def deviner():
    try:
        nombre=int(entree.get())
        if nombre<nombre_secret:
            label_resultat.config(text="le nombre que vous avez donnez est petit")
        elif nombre>nombre_secret:
            label_resultat.config(text="le nombre que vous avez donner est  grand")
        else:
            label_resultat.config(text="bravo vous avez trouver le nombre")
    except valueError:
        label_resultat.config(text="entre un ombre valide")

bouton=tk.Button(fenetre,text="deviner",command=deviner)
bouton.pack(pady=5)

label_resultat=tk.Label(fenetre,text="")
label_resultat.pack(pady=5)

fenetre.mainloop()