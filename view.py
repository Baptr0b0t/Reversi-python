from constants import Black, White, Placeable, Black_view, White_view, Place_view


# Fonction qui affiche un plateau
def affiche_plateau(plateau):
    for ligne in plateau:
        for pion in ligne:
            print("[" + affiche_pion(pion) + "]",end="")
        #retour a la ligne
        print()
    return


# Fonction qui affiche un pion en ASCII
def affiche_pion(pion):
    if pion == Black:
        return Black_view
    elif pion == White:
        return White_view
    elif pion == Placeable:
        return Place_view
    else:
        return " "


# Fonction qui affiche un pion en ASCII
def pion_style(pion):
    if pion == Black:
        return ("White","Black")
    elif pion == White:
        return ("Black","White")
    else:
        return ("Black","Gray")