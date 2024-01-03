from constants import Black,White, Empty
from view import *
from core import *


# Fonction principale
def main():
    # Initialise le plateau de jeu par une matrice
    plateau = [[Empty for i in range(8)] for j in range(8)]

    # Place les pions au centre
    plateau[3][3] = Black
    plateau[4][4] = Black
    plateau[3][4] = White
    plateau[4][3] = White

    
    affiche_plateau(plateau)
    
    affiche_plateau(CheckAllCase(plateau, White))
    Addpion(plateau, White, 2,4)
    affiche_plateau(plateau)
    affiche_plateau(CheckAllCase(plateau, Black))

    


# Exécute la fonction principale
if __name__ == "__main__":
    main()