import sys
# Ajoute le chemin du dossier modules au chemin de recherche des modules
sys.path.append("modules")

import tkinter

from tkinter import *
from tkinter.ttk import *

from constants import font 
from gamemanager import *

# Fonction qui lance le jeu
def lancer_jeu(event):
    #global mode_jeu
    gamemode = mode_jeu.get()
    print(gamemode)
    # Détermine le mode de jeu
    if gamemode == "ordinateur":
        mode = 2
        # Lance le jeu
        print("Lancement du jeu en mode", mode)
        reversi = Reversi(mode)
        fenêtre.destroy()
    elif gamemode == "humain":
        mode = 1
        # Lance le jeu
        print("Lancement du jeu en mode", mode)
        reversi = Reversi(mode)
        fenêtre.destroy()
    else:
        mode = None




# Crée la fenêtre principale
fenêtre = tkinter.Tk()
# Définit les variables globales
mode_jeu = tkinter.StringVar()


fenêtre.geometry('300x220')
fenêtre.resizable(False, False)
fenêtre.title('Radio Button Demo')

style = Style(fenêtre)
style.configure("TRadiobutton", background = "light green", 
                foreground = "red", font = font)
 

# Crée les options
mode_humain = Radiobutton(fenêtre, text="Vs Humain", variable=mode_jeu, value="humain", style="TRadiobutton")
mode_ordinateur = Radiobutton(fenêtre, text="Vs Ordinateur", variable=mode_jeu, value="ordinateur", style="TRadiobutton")



# Ajoute les options a la fenetre 
mode_humain.pack(side=TOP)
mode_ordinateur.pack(side=TOP)

# Crée le bouton "Lancer le jeu"
bouton_lancer = tkinter.Button(fenêtre, text="Lancer le jeu")
bouton_lancer.bind("<Button-1>", lancer_jeu)

# Ajoute le widget à la fenêtre
bouton_lancer.pack()

# Affiche la fenêtre
fenêtre.mainloop()

