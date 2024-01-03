from constants import Black,White, Empty, direction

# Fonction qui ajoute un pion au plateau
def Addpion(plateau, joueur, x, y):
    # Vérifie que le coup est valide
    if not peut_jouer(plateau, joueur, x, y):
        print("Coup invalide.")
        return False

    # Ajoute le pion au plateau
    plateau[x][y] = joueur

    # Le coup a pu être joué
    return True

#Fonction qui vérifie toute les positions 
def CheckAllCase(plateau, joueur):
    CanPlace = [[Empty for i in range(8)] for j in range(8)]
    for x in range(len(plateau)):
        for y in range(len(plateau[0])):
            #print(x,y , peut_jouer(plateau,joueur,x,y))
            if(peut_jouer(plateau,joueur,x,y) == True):
                CanPlace[x][y] = 5
    return CanPlace

# Fonction qui vérifie si un coup est possible
def peut_jouer(plateau, joueur, x, y):
    # Vérifie si la case est vide
    if plateau[x][y] != Empty:
        return False,"Case remplis"
    # Vérifie si le joueur peut capturer des pions
    for dx, dy in direction:
        #print(dx,dy)
        if 0 <= x + dx < 8 and 0 <= y + dy < 8 and plateau[x + dx][y + dy] == (joueur ^ 1):
            # Vérifie si la case i cases devant le pion adverse est occupée par le joueur
            for i in range(1, 8):
                #print("i = ",i )
                if not (0 <= x + dx * i < 8 and 0 <= y + dy * i < 8):

                    #print("case hors plateau", dx * i, dy * i)
                    break

                if plateau[x + dx * i][y + dy * i] == joueur:
                    return True
                elif plateau[x + dx * i][y + dy * i] == Empty:
                    #print("case vide")
                    break
        
    return False,"Pas de capture"