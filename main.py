#def print_hi(name):
#    print(f'Hi, {name}')

def exercice1(): # Demande de saisi de chaîne de caractère et affichage de ces chaînes
    nom = input('- Entrer votre nom : ')
    prenom = input('- Entrer votre prenom : ')
    print('Bonjour '+nom+' '+prenom+'!')

def exercice2(): #Calcul d'une somme de 2 nombres et affichage du résultat
    a = int( input('- Saisir un nombre a : ') )
    b = int( input('- Saisir un nombre b : ') )
    c = a+b
    print('- La sommme des 2 nombres a et b : '+str(c))

def exercice3(): #Calcul d'un maximum entre 2 nombres et affichage du résultat
    a = int(input('- Saisir un nombre a : '))
    b = int(input('- Saisir un nombre b : '))
    c = a + b
    print('- La sommme des 2 nombres a et b : ' + str(c))

if __name__ == '__main__':
    # print_hi('PyCharm')

    print('Exercice 1')
    exercice1()

    print('\nExercice 2')
    exercice2()
