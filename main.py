from constants import Black,White, Empty
from view import *
from core import *
import tkinter

# Fonction principale
def main():

    # Crée une instance de Reversi
    print("create instance")
    reversi = Reversi()
    print("start mainloop")
    #Lance la boucle principale de l'application
    reversi.root.mainloop()


    

class Reversi:
    def __init__(self):
        #super().__init__()
        # Initialise la fenêtre du terminal
        self.root = tkinter.Tk()
        print("create windows")
        # Configure la résolution de la fenêtre
        self.root.geometry("640x680")

        # Empêche l'utilisateur de modifier la résolution
        self.root.resizable(False, False)

        # Crée le plateau de jeu
        # Initialise le plateau de jeu par une matrice
        self.plateau = [[-1 for _ in range(8)] for _ in range(8)]
        
        self.joueur=Black
        # Place les pions au centre
        self.plateau[3][3] = Black
        self.plateau[4][4] = Black
        self.plateau[3][4] = White
        self.plateau[4][3] = White

        print("create button")
        #self.root.focus_set()
        # Crée les boutons du plateau
        self.boutons = []
        for i in range(8):
            for j in range(8):
                _text = affiche_pion(self.plateau[i][j])
                self.boutons.append(tkinter.Button(self.root, text=_text, command= lambda arg1 = (i * 8 + j): self.click(arg1)))
                # Définit la largeur et la hauteur des boutons
                self.boutons[i * 8 + j].config(width=10, height=5)
                # Place les boutons sur le plateau
                self.boutons[i * 8 + j].grid(row=i, column=j)
        
        print(self.plateau)
        #self.Refresh_placeable()

    def Refresh(self):
        for i in range(8):
            for j in range(8):
                _text = affiche_pion(self.plateau[i][j])
                self.boutons[(i * 8 + j)].config(text=_text)

    def Refresh_placeable(self):
        self.Refresh()
        for i in range(8):
            for j in range(8):
                if Can_place(self.plateau, self.joueur, i, j)==True:
                    self.boutons[(i * 8 + j)].config(text="+")
        

    def click(self, coord):
        print(coord)
        
        # Convertit les coordonnées en indices de tableau
        y, x = coord % 8, coord // 8
        print("click", x, y)
        if Can_place(self.plateau, self.joueur, x, y)==True:
            self.plateau[x][y] = self.joueur
            print("placed")
            #self.Refresh()
            self.joueur=self.joueur^1
            self.Refresh_placeable()
            
        

if __name__ == "__main__":
    main()