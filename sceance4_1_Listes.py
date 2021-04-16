def rechercheDansListeNonTrie():
    print("Liste Non Trié :")
    a = 3
    print("-> Recherché : [" + str(a) + "]")
    trouve = -1
    #--
    demo = [4, 3, 1, 9, 12, 11, 6, 37, 28, 7]
    for b in range(0, len(demo)):
        if a == b:
            trouve = b
    # --
    if trouve > -1: print("-> Trouvé : [" + str(trouve) + "]")
    else : print("-> Non trouvé")

def rechercheDansListeTrie():
    print("Liste Trié :")
    a = 9
    print("-> Recherché : [" + str(a) + "]")
    trouve = -1
    #--
    demo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for b in range(0, len(demo)):
        if a == b and b<=20:
            trouve = b
    # --
    if trouve > -1: print("-> Trouvé : [" + str(trouve) + "]")
    else : print("-> Non trouvé")