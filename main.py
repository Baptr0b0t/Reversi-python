from constants import Black,White, Empty
from view import *
from core import *
from computer import *
import sys
# Ajoute le chemin du dossier modules au chemin de recherche des modules
sys.path.append("modules")

import tkinter
from tkinter import *
from tkinter.ttk import *
# Fonction principale
def main():

    # Crée une instance de Reversi
    print("create instance")
    reversi = Reversi()
    print("start mainloop")
    #Lance la boucle principale de l'application
    reversi.root.mainloop()


    

class Reversi:
    def __init__(self, mode_jeu=None):

        if mode_jeu == 1:
            self.mode_jeu = mode_jeu
            print("mode 2joueurs")
        elif mode_jeu == 2:
            self.mode_jeu = mode_jeu
            print("mode ordinateur")
        else:
            print("Le mode de jeu doit être spécifié.")
            exit()



        #super().__init__()
        # Initialise la fenêtre du terminal
        self.root = tkinter.Tk()
        print("create windows")
        # Configure la résolution de la fenêtre
        self.root.geometry("640x680")

        # Empêche l'utilisateur de modifier la résolution
        self.root.resizable(False, False)


        self.joueur=Black

        # Crée le plateau de jeu
        # Initialise le plateau de jeu par une matrice
        self.plateau = [[-1 for _ in range(8)] for _ in range(8)]

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
        self.Refresh()

    def Refresh(self):
        for i in range(8):
            for j in range(8):
                _text = affiche_pion(self.plateau[i][j])
                _foreground, _background = pion_style(self.plateau[i][j])
                self.boutons[(i * 8 + j)].config(text=_text, foreground=_foreground, background=_background)
        self.Refresh_placeable()

    def Refresh_placeable(self):
        #self.Refresh()
        self.placeable_case = []
        self.place=0
        for i in range(8):
            for j in range(8):
                Can_be_place = Can_place(self.plateau, self.joueur, i, j)
                if Can_be_place[0] == True:
                    self.boutons[(i * 8 + j)].config(text="+")
                    self.place=self.place+1
                    if(self.mode_jeu==2):
                        Count=0
                        for direction in Can_be_place[1]:
                            Count= Count + Capture_count(self.plateau, i, j, direction, self.joueur)
                        print("Count for", i,j ,"=",Count)
                        self.placeable_case.append((i * 8 + j, Count))
        if self.place==0:
            self.GameOver()
        print("placeable count", self.placeable_case)

        

    def click(self, coord):
        print(coord)
        
        # Convertit les coordonnées en indices de tableau
        y, x = coord % 8, coord // 8
        print("click", x, y)
        Can_be_place = Can_place(self.plateau, self.joueur, x, y)
        print(Can_be_place)
        if Can_be_place[0] == True:

            
            print("placed")

            #self.plateau[x][y] = self.joueur
            #self.Refresh()
            self.plateau[x][y] = self.joueur
            for direction in Can_be_place[1]:
                print(direction)

                listpond = Capture_list(self.plateau, x, y, direction, self.joueur)
                
                print (listpond)
                self.Setpond(listpond, self.joueur)
                
                    
            affiche_plateau(self.plateau)


            

            
            self.joueur=self.joueur^1
            self.Refresh()
            if self.mode_jeu == 2:
                self.ComputerTurn()

    
    def Setpond(self, listpond, joueur):
        for x,y in listpond:
            print("Capturing", x, y)
            self.plateau[x][y] = joueur

    def LockAllButton(self):
        for i in range(8):
            for j in range(8):
                self.boutons[(i * 8 + j)].config(state=tkinter.DISABLED)

    def UnlockAllButton(self):
        for i in range(8):
            for j in range(8):
                self.boutons[(i * 8 + j)].config(state=tkinter.NORMAL)
    
    def ComputerTurn(self):
        if self.joueur == 1:
            self.LockAllButton()
            self.root.after(3000, self.ComputerAction)
            
    def ComputerAction(self):
        coord = ChoseAction(self.placeable_case)
        y, x = coord % 8, coord // 8
            
        Can_be_place = Can_place(self.plateau, self.joueur, x, y)
            
        if Can_be_place[0] == True:
            self.plateau[x][y] = self.joueur
            for direction in Can_be_place[1]:
                print(direction)

                listpond = Capture_list(self.plateau, x, y, direction, self.joueur)
                    
                print (listpond)
                self.Setpond(listpond, self.joueur)
        else:
            print("Error can't place")
        self.joueur=self.joueur^1
        self.UnlockAllButton()
        self.Refresh()
        
    def GameOver(self):
        print("GameOver")
        self.LockAllButton()
        Count_white=0
        Count_black=0
        Count_empty=0
        for i in range(8):
            for j in range(8):
                if self.plateau[i][j] == White:
                    Count_white = Count_white+1
                elif self.plateau[i][j] == Black:
                    Count_black = Count_black+1
                else:
                    Count_empty = Count_empty+1
        print("White =",Count_white)
        print("Black =",Count_black)
        print("Empty =",Count_empty)
        self.root.after(10000, exit)
    



            
        
        