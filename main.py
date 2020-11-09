from statistics import *
from math import *

#def print_hi(name):
#    print(f'Hi, {name}')

def exercice1():
    print('Exercice 1 - Demande de saisi de chaîne de caractère et affichage de ces chaînes.')
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
    print('Exercice 14 - Saisir un nombre entier n et si ce nombre est un carré parfait ou non')
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
    print(i)
    if i == n:
        print('Le nombre n:'+str(n)+' est un nombre premier')
    else:
        print('Le nombre n:' + str(n) + ' n\'est pas un nombre premier')

if __name__ == '__main__':
    # print_hi('PyCharm')

    exercice15()