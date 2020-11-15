import sys
from statistics import *
from math import *

def print_hi(name):
    print(f'Hi, {name}')

def pythonVersion():
    if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
        print("Python 3.6 or higher is required.")
    else:
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    #sys.exit(1)

def exercice1():
    print('Exercice 1 - Demande de saisi de chaine de caractère et affichage de ces chaine.')
    nom = input('- Entrer votre nom : ')
    prenom = input('- Entrer votre prenom : ')
    print('Bonjour '+nom+' '+prenom+'!')

def exercice2():
    print('Exercice 2 - Calcul d\'une somme de 2 nombres entier et affichage du résultat.')
    a = int(input('- Saisir un nombre entier a : '))
    b = int(input('- Saisir un nombre entier b : '))
    c = a+b
    print('- La sommme de '+str(a)+' et '+str(b)+' est égale à '+str(c))

def exercice3():
    print('Exercice 3 - Calcul d\'un maximum entre 2 nombres entier et affichage du résultat.')
    a = int(input('- Saisir un nombre entier a : '))
    b = int(input('- Saisir un nombre entier b : '))
    if a > b:
        c = 'Le nombre entier a:'+str(a)+' est supérieur à b:'+str(b)+'. Le nombre maximum est a.'
    else:
        c = 'Le nombre entier a:'+str(a)+' est inférieur à b:'+str(b)+'. Le nombre maximum est b.'
    print(c)

def exercice4():
    print('Exercice 4 - Déterminier si un nombre est pair ou impair et afficher le résultat.')
    a = int(input('- Saisir un nombre entier a : '))
    if ( a % 2 ) == 0: # Le modulo est ici utliser pour calculer les le reste avec l'opérateur
        print('Le nombre '+format(a)+' est un nombre pair.')
    else:
        print('Le nombre ' +format(a) + ' est un nombre impair.')

def exercice5():
    print('Exercice 5 - Déterminier si vous êtes mineur ou majeur (age>18 ou age<18) et afficher le résultat.')
    age = int(input('- Saisissez votre âge : '))
    if (age >= 18):
        print('Vous êtes majeur.')
    else:
        print('Vous êtes mineur.')

def exercice6():
    print('Exercice 6 - Calcule d\'un maximum entre 3 nombres et afficher le résultat.')
    x = int(input('- Saisir un nombre entier x : '))
    y = int(input('- Saisir un nombre entier y : '))
    z = int(input('- Saisir un nombre entier z : '))
    if x > y and x > z:
        print('Le nombre entier x:'+str(x)+' est supérieur à y:'+str(y)+' et z:'+str(z)+'. Il est donc le nombre maximum.')
    elif y > x and y > z:
        print('Le nombre entier y:'+str(y)+' est supérieur à x:'+str(x)+' et z:'+str(z)+'. Il est donc le nombre maximum.')
    else:
        print('Le nombre entier z:'+str(z)+' est supérieur à x:'+str(x)+' et y:'+str(y)+'. Il est donc le nombre maximum.')

def exercice7():
    print('Exercice 7 - Afficher les 100 premiers nombres entiers.')
    for i in range(1,100):
        print(i)

def exercice8():
    print('Exercice 8 - Saisir un nombre entier n et afficher la valeur de la somme de 1+2+...+n= .')
    somme = 1
    n = int(input('- Saisir un nombre entier n : '))
    while somme < n:
        somme += 1
    print('La somme totale de n:'+str(n)+' est '+str(somme))

def exercice9():
    print('Exercice 9 - Saisir un nombre entier n et afficher n (->factorielle - type 3!=1x2x3).')
    result = 1
    n = int(input('- Saisir un nombre entier n : '))
    for i in range(n+1):
        if i != 0:
            result *= i
            print('#'+str(i)+' - Le nombre n : '+str(result))

def exercice10():
    print('Exercice 10 - Saisir le rayon d\'un cercle et afficher la surface et le périmètre de celui-ci.')
    rayon = int(input('- Saisir le rayon d\'un cercle (entier) : '))
    pi = 3.14
    surface = rayon**2 * pi
    perimetre = rayon * pi * 2
    print('La surface est de '+str(surface)+' et le périmètre est de '+str(perimetre)+'.')

def exercice11():
    # Source de révison : http://villemin.gerard.free.fr/aInforma/PYTHON/Arithmet.htm
    print('Exercice 11 - Saisir un nombre entier et afficher tous les diviseurs de ce nombre.')
    diviseurs = []
    n = int(input('- Saisir un nombre entier n : '))
    for i in range(1,n+1):
        if n%i == 0:
            diviseurs.append(i)
    print('Les diviseurs du nombre n:'+str(n)+' sont : \n'+str(diviseurs))

def exercice12():
    print('Exercice 12 - Saisir un nombre entier n, afficher la table de multiplicatoin de n .\nOu toutes les tables de multiplications.')
    choix = int(input('-> 1 : Afficher la table de multiplication d\'un nombre n .\n-> 2 : Afficher toutes les tables de multiplication. \nVotre choix : '))
    if choix == 1:
        n = int(input('- Saisir un nombre entier n : '))
        for i in range(0, 11):
            result = n * i
            print('' + str(n) + ' * ' + str(i) + ' = ' + str(result) + '')
    elif choix == 2:
        listeDesTablesDeNombreEntiers = [0,1,2,3,4,5,6,7,9,10]
        for list in listeDesTablesDeNombreEntiers:
            tableTmp = []
            for i in range(0, 11):
                result = list * i
                tableTmp.append(result)
            print('Table de '+str(list)+' : '+str(tableTmp))
    else:
        print('Le choix que vous avez saisi n\'éxiste pas.')

def exercice13():
    print('Exercice 13 - Saisir 2 nombres entiers a et b et afficher le quotient et le reste de la division euclidienne de a par b')
    a = int(input('- Saisir un nombre entier a : '))
    b = int(input('- Saisir un nombre entier b : '))
    c = a // b #Calcul du quotient ( // -> permet d'obtenir un nombre entier)
    d = a % b #Calcul du reste
    print('- Le quotient de ' + str(a) + ' et ' + str(b) + ' est égale à ' + str(c)+' et le reste de celle-ci est '+str(d))

def exercice14():
    # Carré parfait : un nombre entier est divisible par lui même et par 1
    print('Exercice 14 - Saisir un nombre entier n et déterminer si ce nombre est un carré parfait ou non')
    n = int(input('- Saisir un nombre entier n : '))

    #--Derminer les diviseur d'un nombre |PARTIE ENCORE EN DEV|
    x = 1
    listeDiviseurs = []
    while x <= n:
        result = n % x
        for verifListDiviseurs in listeDiviseurs:
            if result in verifListDiviseurs and listeDiviseurs is None:
                listeDiviseurs.append(result) #bloque ici
        x += 1
    #print(listeDiviseurs)
    #--
    #print(n / n)
    #print(n % n)
    #print(n / 1)
    #print(n % 1)
    #--

    if n % n == 0 and n / n == 1:
        print('Le nombre n:'+str(n)+' est un carré parfait car il est divible par lui même.')
    else:
        print('Le nombre n:' + str(n) + ' n\'est pas un carré parfait car il n\'est pas divible par lui même.')

def exercice15():
    # Un nombre premier est un nombre entier naturel (non nul) qui admet exactement 2 diviseurs distincts : 1 et lui-même. Soit un divisible seulement par 1 et lui-même.
    # Liste des nombres premiers - source : https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Primencomposite0100.png/330px-Primencomposite0100.png
    print('Exercice 15 - Saisir un nombre n et déterminier si ce nombre est premier ou non')
    n = int(input('- Saisir un nombre entier n : '))
    i = 2
    while i < n and n % i != 0:
         i += 1
    #print(i)
    if i == n:
        print('Le nombre n:'+str(n)+' est un nombre premier')
    else:
        print('Le nombre n:' + str(n) + ' n\'est pas un nombre premier')

def exercice16():
    print('Exercice 16 - Saisir une chaine de caractère s et afficher les caractère d\'un variable de typpe chaine de cractères')
    s = input("- Saisir chaine de cractère : ")
    for caractereInS in s:
        print(caractereInS)
    print('Voici ci-dessus tous les caratères composant votre chaine de caractère s:' + str(s) + '.')

def exercice17():
    print('Exercice 17 - Saisir une chaine de cractère s et afficher le nombre d’occurrences de chaque caractère dans la chaine')
    s = 'itescia.fr'
    #Création de la liste des caractères
    listeCaracteres = []
    for caractereInS in s:
        caractereExistant = 0
        #vérification du caractère dans la liste si existant
        for caractereInlisteCaracteres in listeCaracteres:
            if caractereInlisteCaracteres == caractereInS:
                caractereExistant = 1
                #print(caractereInlisteCaracteres+'-'+caractereInS)
        #print(str(caracterInS)+'-'+str(caractereExistant))
        if caractereExistant == 0:
            listeCaracteres.append(caractereInS)
    print(listeCaracteres)
    #vérification des occurences d'un caractère par rapport à la chaine de caractère saisi et affichage
    longueurDeLaListeCaracteres = len(listeCaracteres)
    x = 0
    while x < longueurDeLaListeCaracteres:
        totalOccurencesCaracteres = str(s.count(listeCaracteres[x]))
        print('Le caractère : ” '+str(listeCaracteres[x])+' ” figure '+str(totalOccurencesCaracteres)+' fois.')
        x += 1
    print('Voici ci-dessus tous les occurences d\'un caractère composant votre chaine de caractère s:' + str(s) + '.')

def exercice18():
    print('Exercice 18 - Saisir une chaine de caractère "s" pour vérifier \'existance d\'un caractère "a" dans celle-ci, ainsi que sa possition si existant')
    s = input("- Saisir chaine de caractère : ")
    listeCaracteres = []
    caractereRechercher = 'a'
    caractereExistant = 0
    postionCaractereInS = []
    totalOccurencesCaractereRechercher = 0
    # Transformation de la chaine de caractère en liste
    for caractereInS in s:
        listeCaracteres.append(caractereInS)
    #print(listeCaracteres)
    # vérification du cractère dans la liste si existant
    for index, value in enumerate(listeCaracteres): #Récupère la position et la valeur d'un liste
        #print(index, value)
        if caractereRechercher == value:
            caractereExistant = 1
            totalOccurencesCaractereRechercher = listeCaracteres.count(str(caractereRechercher))
            postionCaractereInS.append(index)
    if caractereExistant == 1:
        print('La lettre a apparait '+str(totalOccurencesCaractereRechercher)+' fois et se trouve à la postition '+str(postionCaractereInS)+'.')
    else:
        print('La lettre a n\'éxiste pas dans la chaine de caractère saisi.')
    # Fonctionnel aussi avec une phrase tel que : L'avion apparaitra dans les airs et il sera blanc.

def exercice19():
    print('Exercice 19 - Lister les chaines qui composent la liste l = [“laptop”, “iphone”, “tablet”] et indiquer la longueur de chaque chaine')
    l = ['laptop', 'iphone', 'tablet']
    #Découpage de chaque chaines de caractère dans la liste pour les lister
    x = 0
    toutesListes = []
    while x < len(l):
        listeTmp = []
        for liste in l[x]:
            listeTmp.append(liste)
            #print(liste)
        toutesListes.extend([listeTmp])
        print('La chaine '+str(l[x])+' à une longueur de '+str(len(l[x]))+' et se compose de '+str(toutesListes[x])+'.')
        x += 1
    #print(toutesListes)

def exercice20():
    print('Exercice 20 - Saisir une chaine de caractère pour remplacer le premier caractètre d\'une chaine par le dernier')
    s = input("- Saisir chaine de caractère : ")
    listeDesCaracteresInS = []
    for caracteresInS in s:
        listeDesCaracteresInS.append(caracteresInS)
    print('Chaine avant inversion : '+str(s))
    #Récupération de la position du dernier caractère
    positionDernierCaractereInS = len(s)-1
    #Récupération du premier et dernier caractère dans la chaine saisi
    premierCaractereInS = listeDesCaracteresInS[0]
    dernierCaractereInS = listeDesCaracteresInS[positionDernierCaractereInS]
    #Inversion des caractères entre le permier et dernier
    newPremierCaractereInS = dernierCaractereInS
    newDernierCaractereInS = premierCaractereInS
    #Remplacemement des anciens caractères dans la chaine par les nouveaux
    listeDesCaracteresInS[0] = newPremierCaractereInS
    listeDesCaracteresInS[positionDernierCaractereInS] = newDernierCaractereInS
    newS = ''
    for generationNewS in listeDesCaracteresInS:
        newS += str(generationNewS)
    #--
    print('Chaine après inversion : '+str(newS)+'.')
    #--CODE-EXERCICE-20-A-SIMPLIFIER--#

def exercice21():
    print('Exercice 21 - Compter le nombre de voyelle dans la chain de caractère s=‘anticonstitutionellement’')
    s = 'anticonstitutionellement'
    voyelles = ['a','e','i','o','u','y']
    ttlVoyelles = 0
    #Lecture des caractères de la chaine
    for caractersInS in s:
        rechercheVoyelle = caractersInS
        #Comparaison avec la liste des voyelles
        for compareVoyelle in voyelles:
            if compareVoyelle == rechercheVoyelle:
                ttlVoyelles += 1
    print('La chaine '+str(s)+' possède '+str(ttlVoyelles)+' voyelles.')

def exercice22():
    print('Exercice 22 - Afficher le permier d\'un text tel que : t = Python est un merveilleux langage de programmation')
    t ='Python est un merveilleux langage de programmation'
    decoupeText = t.split(' ')
    print('Le premier de la chaine est '+str(decoupeText[0])+'.')

def exercice23():
    print('Exercice 23 - Afficher l\'extension d\'un fichier')
    s = input("- Saisir un fichier son extension : ")
    decoupeText = s.split('.')
    print('L\'extension du fichier est ' + str(decoupeText[1]) + '.')

def exercice24():
    #Un palindrome est un mot dont l’ordre des lettres reste le même si on le lit de gauche à droite ou de droite à gauche.
    #Par exemple : ‘laval’ , ‘radar, ‘sos’… sont des palindromes.
    print('Exercice 24 - Saisi d\'un mot et vérification si s\'est un palindrome')
    s = input("- Saisir un mot : ")
    # --
    listeCaracteresInS = []
    nombreTotalDeCaractereInS = 0
    for index, value in enumerate(s):  # Récupère la position et la valeur d'un liste
        #print(str(index) + "," + str(value))
        listeCaracteresInS.extend([[index, value]])
        nombreTotalDeCaractereInS += 1
    #--
    demiDuNombreTotalDeCaractereInS = int(nombreTotalDeCaractereInS / 2)
    #print('liste : ' + str(listeCaracteresInS))
    #print('total : ' + str(nombreTotalDeCaractereInS))
    #print('moitié total : '+str(demiDuNombreTotalDeCaractereInS))
    #--
    premierCaractere = 0
    dernierCaractere = nombreTotalDeCaractereInS-1
    #Vérification des caractères similaires
    similariees = 0
    while premierCaractere < float(demiDuNombreTotalDeCaractereInS+0.5):
        if listeCaracteresInS[premierCaractere][1] == listeCaracteresInS[dernierCaractere][1]:
        #    print('1er : ' + str(listeCaracteresInS[premierCaractere][1]) + ' et dernier : ' + str(listeCaracteresInS[dernierCaractere][1])+' - ok')
            similariees += 1
        #else:
        #    print('1er : ' + str(listeCaracteresInS[premierCaractere][1]) + ' et dernier : ' + str(listeCaracteresInS[dernierCaractere][1])+' - no')
        premierCaractere += 1
        dernierCaractere -= 1
    # Vérification des similaritées trouvées
    if similariees == demiDuNombreTotalDeCaractereInS+1:
        print('Le mot saisi est un palindrome.')
    else:
        print('Le mot saisi n\'est pas un palindrome.')

def exercice25():
    print('Exercice 25 - Saisir un mot et afficher son inverse.')
    s = input("- Saisir un mot : ")
    # Récupération des caractères de la chaine saisi
    listeCaracteresInS = []
    nombreTotalDeCaractereInS = len(s)
    for index, value in enumerate(s):  # Récupère la position et la valeur d'un liste
        listeCaracteresInS.extend([[index, value]])
    #print(listeCaracteresInS)
    #Retounrnement des caractères de la chaine saisi
    inverseListeCaractereInS = []
    x = 0
    while nombreTotalDeCaractereInS > 0:
        #print(listeCaracteresInS[nombreTotalDeCaractereInS-1][0])
        inverseListeCaractereInS.extend([[ x , str(listeCaracteresInS[nombreTotalDeCaractereInS-1][1]) ]])
        nombreTotalDeCaractereInS -= 1
        x += 1
    #print(inverseListeCaractereInS)
    # Constructione de la chaine inverse
    y = 0
    inverseDuMotS = ''
    for inverse in inverseListeCaractereInS:
        inverseDuMotS = inverseDuMotS+inverse[1]
        y += 1
    print('L\'inverse du mot '+s+' est '+inverseDuMotS)

def exercice26():
    print('Exercice 26 - Saisir un text et afficher tous les mots commençant pas la lettre a.')
    # texte de test simple : mon avion est bleu avec des ails rouge
    s = input("- Saisir d'un texte : ")
    #separation des mots du texte saisi
    listeMots = s.split(' ')
    print(listeMots)
    #comptage des mots récupérer
    totalMotsInS = 0
    for mots in listeMots:
        totalMotsInS += 1
    print(totalMotsInS)
    #Affichage de mots commençant par a
    x = 0
    while x < totalMotsInS:
        motSelected = []
        for mots in listeMots[x]:
            motSelected.append(mots)
        if motSelected[0] == 'a':
            print('Le mot '+str(x)+':'+str(listeMots[x])+' commence par la lettre a.')
        x += 1
    #--
    #caracteresDeSeprartionComplexe = ['(', ')', '_', '-', ':', ';', '.', '\'', ' ']
    #texte de test complexe : j'ai_un-vélo;rouge.et:bleu(si,un avion\vole)

def exercice27():
    print('Exercice 27 - Chercher le mot le plus long sur une chaine s.')
    s = input("- Saisir d'un texte : ")
    # separation des mots du texte saisi
    listeMots = s.split(' ')
    #print(listeMots)
    # Affichage du mot le plus long
    for mots in listeMots:
        print('Le mot '+str(mots)+' a une longueur de '+str(len(mots))+'.')

def exercice28():
    print('Exercice 28 - Tester si une liste ou une chaine de caractère est vide ou non.')
    s = input("- Saisir une liste ou chaine de caractère : ")
    if s is not None and s != '':
        print('La liste ou la chaine de caractère saisi n\'est pas vide et contient :\n--> '+str(s))
    else:
        print('La liste ou la chaine de caractère saisi est vide.')


if __name__ == '__main__':
    #print_hi('PyCharm')
    #pythonVersion()

    exercice28()

    # Git Version : v0.8