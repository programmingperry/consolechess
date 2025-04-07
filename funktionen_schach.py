import numpy as np
# Quellen 2D Listen:
# https://bjc.edc.org/March2019/bjc-r/cur/programming/old-labs/python/2D_lists.html?topic=nyc_bjc%2FNA-python.topic
def startaufstellung():
    figuren = np.array([['t', 's', 'l', 'd', 'k', 'l', 's', 't'],
                        ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
                        ['T', 'S', 'L', 'D', 'K', 'L', 'S', 'T']])
    return figuren 

def zugeingabe(spieler):
    return input(f'{spieler} ist am Zug\n>>> ')

def zugbereinigung(zugeingabe):
    zugbereinigung = zugeingabe.lower()
    bereinigung = [' ', '-']
    zugeingabe = ''
    for i in range(len(zugbereinigung)):
        if zugbereinigung[i] not in bereinigung:
            zugeingabe = zugeingabe + zugbereinigung[i]
    return zugeingabe

def eingabepruefung(zugeingabe):
    feldkorBuchstaben = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    feldkorZahlen = ['1', '2', '3', '4', '5', '6', '7', '8']
    if (zugeingabe[0] and zugeingabe[2]) in feldkorBuchstaben and (zugeingabe[1] and zugeingabe[3]) in feldkorZahlen:
        return True 
    else:
        return False

def schachbrett(array):
    print('\n      A        B        C        D        E        F        G        H       ')
    print(' +------------------------------------------------------------------------+')
    print(' |         #########         #########         #########         #########|')
    print(f'8|    {array[0,0]}    ### {array[0,1]} ###    {array[0,2]}    ### {array[0,3]} ###    {array[0,4]}    ### {array[0,5]} ###    {array[0,6]}    ### {array[0,7]} ###|8')
    print(' |         #########         #########         #########         #########|')
    print(' |#########         #########         #########         #########         |')
    print(f'7|### {array[1,0]} ###    {array[1,1]}    ### {array[1,2]} ###    {array[1,3]}    ### {array[1,4]} ###    {array[1,5]}    ### {array[1,6]} ###    {array[1,7]}    |7')
    print(' |#########         #########         #########         #########         |')
    print(' |         #########         #########         #########         #########|')
    print(f'6|    {array[2,0]}    ### {array[2,1]} ###    {array[2,2]}    ### {array[2,3]} ###    {array[2,4]}    ### {array[2,5]} ###    {array[2,6]}    ### {array[2,7]} ###|6')
    print(' |         #########         #########         #########         #########|')
    print(' |#########         #########         #########         #########         |')
    print(f'5|### {array[3,0]} ###    {array[3,1]}    ### {array[3,2]} ###    {array[3,3]}    ### {array[3,4]} ###    {array[3,5]}    ### {array[3,6]} ###    {array[3,7]}    |5')
    print(' |#########         #########         #########         #########         |')
    print(' |         #########         #########         #########         #########|')
    print(f'4|    {array[4,0]}    ### {array[4,1]} ###    {array[4,2]}    ### {array[4,3]} ###    {array[4,4]}    ### {array[4,5]} ###    {array[4,6]}    ### {array[4,7]} ###|4')
    print(' |         #########         #########         #########         #########|')
    print(' |#########         #########         #########         #########         |')
    print(f'3|### {array[5,0]} ###    {array[5,1]}    ### {array[5,2]} ###    {array[5,3]}    ### {array[5,4]} ###    {array[5,5]}    ### {array[5,6]} ###    {array[5,7]}    |3')
    print(' |#########         #########         #########         #########         |')
    print(' |         #########         #########         #########         #########|')
    print(f'2|    {array[6,0]}    ### {array[6,1]} ###    {array[6,2]}    ### {array[6,3]} ###    {array[6,4]}    ### {array[6,5]} ###    {array[6,6]}    ### {array[6,7]} ###|2')
    print(' |         #########         #########         #########         #########|')
    print(' |#########         #########         #########         #########         |')
    print(f'1|### {array[7,0]} ###    {array[7,1]}    ### {array[7,2]} ###    {array[7,3]}    ### {array[7,4]} ###    {array[7,5]}    ### {array[7,6]} ###    {array[7,7]}    |1')
    print(' |#########         #########         #########         #########         |')
    print(' +------------------------------------------------------------------------+')
    print('      A        B        C        D        E        F        G        H       \n')

schachbrett(startaufstellung())

