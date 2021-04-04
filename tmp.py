
    tmp = []
    for mots in listeMots:
        if listeMots.count(mots) > 1:


    #Création de la liste des mots avec leur position
    listeMotsEtPosition = []
    for index, value in enumerate(listeMots):  # Récupère la position et la valeur d'un liste
        motExistant = 0
        for checkMot in listeMotsEtPosition:
            if checkMot == value:
                motExistant = 1
        if motExistant == 0:
            listeMotsEtPosition.extend([[index, value]])
    print('-'+str(listeMotsEtPosition))

    # comptage des mots récupérer
    totalMotsInS = 0
    #for mots in listeMots:
    #    totalMotsInS += 1
    #print(totalMotsInS)

    listNombreExistantMotsInS = []
    for mots in listeMotsEtPosition:
        print(str(mots)+' appartait '+str(listeMots.count(mots))+' fois')
        if listeMots.count(mots) > 1:
            noExistance = 0
            if listNombreExistantMotsInS and listNombreExistantMotsInS != '': #Vérification d'un liste vide
                noExistance = 1
                print(listNombreExistantMotsInS)
            if noExistance == 0:
                listNombreExistantMotsInS.append([ [mots,listeMots.count(mots)] ])
    print(listNombreExistantMotsInS)

    #Génération d'une liste d'existance
    #listNombreExistantMotsInS = []
    #x = 0
    #for mots in listeMots:
    #    print(str(mots) + ' ' + str(listNombreExistantMotsInS))
    #    if x > 0:
    #        #f listNombreExistantMotsInS[x] == mots:
    #        listNombreExistantMotsInS.extend([[mots,0]])
    #    x += 1
    #print(listNombreExistantMotsInS)

    #Mise à jour du nombre d'éxistance de chaque mots
    #y = 1
    #while y < totalMotsInS:
    #    for mots in listeMots:
    #        #print('listeMots[y] : '+listeMots[y]+' \n mot : '+mots+'')
    #        if listeMots[y] == mots:
    #            listNombreExistantMotsInS[y] += 1
    #            print('ok')
    #    y += 1
    #print(listNombreExistantMotsInS)
    #Affichage du nombre d'éxistance de chaque mots