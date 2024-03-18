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

    

class Reversi:
    def __init__(self, mode_jeu=None):
        self.running=True
        if mode_jeu == 1:
            self.mode_jeu = mode_jeu
            print("2 players mode set")
        elif mode_jeu == 2:
            self.mode_jeu = mode_jeu
            print("Computer mode set")
        else:
            raise Exception("Gamemode need to be specified.")



        # Initialise la fenêtre du terminal
        self.root = tkinter.Tk()
        print("creating windows")
        # Configure la résolution de la fenêtre
        self.root.geometry("560x600")

        # Empêche l'utilisateur de modifier la résolution
        self.root.resizable(False, False)
        self.root.title("Reversi")
        # Set le joueur actuel
        self.joueur=Black

        # Crée le plateau de jeu
        # Initialise le plateau de jeu par une matrice
        self.plateau = [[-1 for _ in range(8)] for _ in range(8)]

        # Place les pions au centre
        self.plateau[3][3] = Black
        self.plateau[4][4] = Black
        self.plateau[3][4] = White
        self.plateau[4][3] = White

        print("creating all button")
        #self.root.focus_set()
        # Crée les boutons du plateau
        self.boutons = []
        for i in range(8):
            for j in range(8):
                _text = affiche_pion(self.plateau[i][j])
                
                self.boutons.append(tkinter.Button(self.root, text=_text, command= lambda arg1 = (i * 8 + j): self.click(arg1)))
                # Définit la largeur et la hauteur des boutons
                self.boutons[i * 8 + j].config(width=8, height=4)
                # Place les boutons sur le plateau
                self.boutons[i * 8 + j].grid(row=i, column=j)
        
        #print(self.plateau)
        self.Refresh()

    def Refresh(self):
        #Modifie tout les pions de l'interface pour correspondre au plateau
        for i in range(8):
            for j in range(8):
                _text = affiche_pion(self.plateau[i][j])
                _foreground, _background = pion_style(self.plateau[i][j])
                self.boutons[(i * 8 + j)].config(text=_text, foreground=_foreground, background=_background)
        self.Refresh_placeable()


    def Refresh_placeable(self):
        #Trouve les cases pouvant accueilir un pion
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
            if self.Passturned == 3:
                self.GameOver()
            else:
                self.Passturned = self.Passturned + 1
                self.Passturn()
        else:
            self.Passturned = 0
            self.UnlockAllButton()
        print("placeable count", self.placeable_case)

        

    def click(self, coord):
        #print(coord)
        
        # Convertit les coordonnées en indices de tableau
        y, x = coord % 8, coord // 8
        print("click", x, y)
        Can_be_place = Can_place(self.plateau, self.joueur, x, y)
        #print(Can_be_place)
        if Can_be_place[0] == True:

            
            print("placed", x,y)

            #self.plateau[x][y] = self.joueur
            #self.Refresh()
            self.plateau[x][y] = self.joueur
            for direction in Can_be_place[1]:
                #print(direction)

                listpond = Capture_list(self.plateau, x, y, direction, self.joueur)
                
                #print (listpond)
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
            self.root.after(1500, self.ComputerAction)
            
    def ComputerAction(self):
        if(self.running==False):
            return
        coord = ChoseAction(self.placeable_case)
        y, x = coord % 8, coord // 8

        Can_be_place = Can_place(self.plateau, self.joueur, x, y)
                
        if Can_be_place[0] == True:
            self.plateau[x][y] = self.joueur
            for direction in Can_be_place[1]:
                #print(direction)

                listpond = Capture_list(self.plateau, x, y, direction, self.joueur)
                        
                #print(listpond)
                self.Setpond(listpond, self.joueur)
        else:
            raise Exception("Can't place")
        self.joueur=self.joueur^1
        self.Refresh()


    def Passturn(self):
        self.LockAllButton()
        self.joueur=self.joueur^1
        self.Refresh()


    def GameOver(self):
        print("GameOver")
        self.LockAllButton()
        self.running=False
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
        result = (Count_white, Count_black, Count_empty)
        self.root.after(4000, self.ShowResult, result)
        
    
    def ShowResult(self, result_tupple):
        Count_white = str(result_tupple[0])
        Count_black = str(result_tupple[1])
        Count_empty = str(result_tupple[2])


        if(Count_white>Count_black):
            winner="White"
        elif(Count_white==Count_black):
            winner="Draw"
        elif(Count_white<Count_black):
            winner="Black"

        self.result = tkinter.Tk()
        print("creating result windows")
        # Configure la résolution de la fenêtre
        self.result.geometry("300x200")

        # Empêche l'utilisateur de modifier la résolution
        self.result.resizable(False, False)
        self.result.title("Reversi Result")
        
        # Créer des labels 
        self.label_1 = tkinter.Label(self.result, text="Count_white : " + Count_white, background="white",
            foreground="black").pack()
        self.label_2 = tkinter.Label(self.result, text="Count_black : " + Count_black, background="black",
            foreground="white").pack()
        self.label_3 = tkinter.Label(self.result, text="Count_empty : " + Count_empty, background="gray",
            foreground="black").pack()
        self.label_4 = tkinter.Label(self.result, text="Winner : " + winner, foreground="gold", font=("Arial", 20)).pack()
        
        self.result.mainloop()
        



            
        
        