# Objectif Séance 2
#   - Partie 1
#       - Exerice 1 - Le chiffre porte bonheur
#           Un chiffre porte bonheur est un nombre entier qui, lorsqu'on ajoute les carrés de chacun de ses chiffres,
#           puis les carrés de ce résultat et ainsi jusqu'à l'obtention d'un nombre à un seul chiffre égal à 1.
#
# Outil d'apprentissage : Les fonctions => https://youtu.be/tIuFA2rxUZE

def conversionNombreVersListe(chaineNombre):
    #Création d'une liste de chiffres qui compose le nombre
    listeChiffres = []
    for chiffre in chaineNombre:
        listeChiffres.append(int(chiffre)) #conversion de la chaine de caractère entier par int()
    print('- listeChiffres : '+str(listeChiffres))
    return listeChiffres

def passageAuCarreListeChiffres(longueurDuNombre, listeChiffres):
    #Passage au carré des chiffre et calcul de leur somme
    x = 0
    listeChiffresAuCarre = []
    sommeDesCarre = 0
    while x < longueurDuNombre:
        sommeDuChiffreAuCarre = listeChiffres[x] ** 2
        listeChiffresAuCarre.append(int(sommeDuChiffreAuCarre))
        sommeDesCarre += sommeDuChiffreAuCarre
        x += 1
    print('- listeChiffresAuCarre : '+str(listeChiffresAuCarre)+' - sommeDesCarre '+str(sommeDesCarre))
    return sommeDesCarre

def chiffrePorteBonheur(nombre):
    print('Scéance 2 - Exercice 1 - Le chiffre porte bonheur')
    print('Le nombre saisi est '+str(nombre))

    chaineNombre = str(nombre) #Conversion d'un nombre en chaine de caractère
    longueurDuNombre = len(chaineNombre) #Récupération de la longueur du nombre

    listeChiffres = conversionNombreVersListe(chaineNombre)
    sommeDesCarre = passageAuCarreListeChiffres(longueurDuNombre, listeChiffres)

    while sommeDesCarre >= 10:
        #Vérification de la somme si inférieur à 10
        if sommeDesCarre >= 10:
            print('-> La somme '+str(sommeDesCarre)+' est supérieur à 10.')
            chaineNombre = str(sommeDesCarre)  # Conversion d'un nombre en chaine de caractère
            longueurDuNombre = len(chaineNombre)  # Récupération de la longueur du nombre
            listeChiffres = conversionNombreVersListe(chaineNombre)
            sommeDesCarre = passageAuCarreListeChiffres(longueurDuNombre, listeChiffres)

    if sommeDesCarre <= 10:
        print('-> La somme '+str(sommeDesCarre)+' est inférieur à 10.')
