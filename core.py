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

def Capture_list(plateau, x, y, direction, joueur):
    capture_list=[]
    dx=direction[0]
    dy=direction[1]
    i=1
    while (0 <= x + dx * i < 8 and 0 <= y + dy * i < 8) and plateau[x + dx * i][y + dy * i] != joueur:
        capture_list.append((x + dx * i, y + dy * i))
        i=i+1
    print(capture_list)
    return capture_list

            


# Fonction qui vérifie si un coup est possible
def Can_place(plateau, joueur, x, y):
    capture=0
    capture_list=[]
    # Vérifie si la case est vide
    if plateau[x][y] != Empty:
        return False,"Case remplis"
    # Vérifie si le joueur peut capturer des pions
    for dx, dy in direction:
        #print(dx,dy)
        if 0 <= x + dx < 8 and 0 <= y + dy < 8 and plateau[x + dx][y + dy] == (joueur ^ 1):
            # Vérifie si la case libre est a cote (dans la direction) d'une case occupée par le joueur adverse
            capturing=True
            i=1
            while (0 <= x + dx * i < 8 and 0 <= y + dy * i < 8) and capturing==True :
                
                #print("i =",i )


                if plateau[x + dx * i][y + dy * i] == joueur:
                    #deuxieme pion detecter
                    #print("capture", i)
                    capture = capture + (i-1)
                    capture_list.append((dx, dy))
                    capturing=False
                elif plateau[x + dx * i][y + dy * i] == Empty:
                    #print("case vide")
                    capturing=False
                #Continue la capture
                elif plateau[x + dx * i][y + dy * i] == (joueur ^ 1):
                    i=i+1

                
    #print("capture count", capture)
    if capture>0:
        #print(capture_list)
        return True, capture_list
    else:
        return False,"Pas de capture"