from constants import Black,White, Empty, direction

# Fonction qui ajoute un pion au plateau
def Addpion(plateau, joueur, x, y):
    # Vérifie que le coup est valide
    if not Can_place(plateau, joueur, x, y):
        print("Coup invalide.")
        return False

    # Ajoute le pion au plateau
    plateau[x][y] = joueur

    # Le coup a pu être joué
    return True

#Fonction qui vérifie toute les positions 
def CheckAllCase(plateau, joueur):
    CanPlace = [[Empty for i in range(8)] for j in range(8)]
    for x in range(8):
        for y in range(8):
            print(x,y , Can_place(plateau,joueur,x,y))
            if(Can_place(plateau,joueur,x,y) == True):
                CanPlace[x][y] = 5
    return CanPlace

# Fonction qui vérifie si un coup est possible
def Can_place(plateau, joueur, x, y):
    capture=0
    # Vérifie si la case est vide
    if plateau[x][y] != Empty:
        return False,"Case remplis"
    # Vérifie si le joueur peut capturer des pions
    for dx, dy in direction:
        #print(dx,dy)
        if 0 <= x + dx < 8 and 0 <= y + dy < 8 and plateau[x + dx][y + dy] == (joueur ^ 1):
            # Vérifie si la case i cases devant le pion adverse est occupée par le joueur
            
            for i in range(8):
                capturing=True
                #print("i = ",i )
                if not (0 <= x + dx * i < 8 and 0 <= y + dy * i < 8):

                    #print("case hors plateau", dx * i, dy * i)
                    capturing=False

                if capturing==True and plateau[x + dx * i][y + dy * i] == joueur:
                    #deuxieme pion detecter
                    #print("capture", i)
                    capture = capture + i
                elif capturing==True and plateau[x + dx * i][y + dy * i] == Empty:
                    #print("case vide")
                    capturing=False

                
    #print("capture count", capture)
    if capture>0:
        return True
    else:
        return False,"Pas de capture"