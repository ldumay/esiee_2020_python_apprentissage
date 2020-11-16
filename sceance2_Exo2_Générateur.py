# - Partie 1 - Exerice 1 - Le chiffre porte bonheur Étant donné un générateur g qui fournit la séquence : a, b, c, d,
# e, ..., construire un générateur g2 qui donne a, a, b, b, c, c, d, d, e, e, ... Généraliser pour la réplication non
# pas deux, mais un nombre arbitraire, paramétrable, de fois. Itérer l'original g dans g2 ==> C'est à dire : Générer
# une réplication n fois un séquence tel que g = [a,b,c,d,e,..] -> g2 = [a,a,b,b,c,c,d,d,e,e,...]
#
# Outil d'apprentissage : Les générateurs => https://www.youtube.com/watch?v=dyFVeV6O2rc et https://youtu.be/r2ywKv9gaJ4
#   -> Paramètres variables d'une fonction

from ldumay_dictionnaires import *

def gen():
    yield 'a'
    yield 'b'
    yield 'c'

def generateur(*args, **kwargs):
    #Vérification des variables saisi
    #Paramètre du nombre de génération
    if args[0] is not None:
        nGenerator = args[0]
    else:
        nGenerator = 1
    # Paramètre du du dictionnaire
    if args[1] is not None:
        chaine = args[1]
    else:
        chaine = dictionnaireAlphabetique()

    #print(args)
    print('Chaine insérée : '+str(chaine)+' - Nombre de généteur demander : '+str(nGenerator))

    g = gen()
    for h in g:
        print(h)


# - - - - Prof - Explication 1 - - - -
#def generateur():
#    yield "a"
#    yield "b"
#    yield "c"
#
#i=generateur()
#for v in i:
#       print(v)
#
#ca t'affichera a puis b puis c
#un generateur c'est comme une liste déja remplie
#
#un bon exemple
#https://python.doctor/page-iterateurs-iterator-generateur-generator-python

# - - - - Prof - Explication 2 - - - -

#au départ fais un générateur qui genere les lettres a, b, c

#ensuite tu poursuis l'exo il te faut un gen2 qui appelle gen pour doubler les lettres , donc quand l'appelle a gen te sort a, gen 2 te sort a a

#ensuite faut ajouter un param pour que gen2 te sorte a a a si le param vaut 3
#il triplera ou quadruplera etc...en fonction de ce que tu lui passes