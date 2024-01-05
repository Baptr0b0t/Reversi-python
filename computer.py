import random
import time
def ChoseAction(placeable_case):
    max_value=0
    best_coord_list=[]
    redo=True
    while redo==True:
        redo=False
        for value in placeable_case:
            if value[1]==max_value:
                best_coord_list.append(value[0])
            elif value[1]>max_value:
                max_value=value[1]
                best_coord_list=[]
                redo=True
        print("Choise best Coord_list", best_coord_list)
    if len(best_coord_list)>=1:
        return random.choice(best_coord_list)
    else:
        print('error : no good solution')
        



