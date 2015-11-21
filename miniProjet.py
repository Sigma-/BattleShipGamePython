# -*- coding: utf-8 -*-
# BattleShip Game Python

def display_map(own_map) :
    """Diplay the Battleship Map
    Parameters :
    ------------
    own_map : your own map given by the file (list)
    
    Returns :
    ---------
    own_map : your own map (list)
    
    """
    print "  A B C D E F G H I J"
    for i,j in enumerate(own_map):
        print i,' '.join(j)
        