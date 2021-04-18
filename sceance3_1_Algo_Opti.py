# Algorithmie Quadratique Simple Tableau
def exempleAlgoQuadratiqueSimple():
    tab = [0, 1, 2, 3, 4, 5]
    n=5
    e=0
    for i in range(0,n):
        if tab[i] == e:
            print("OK - i = "+str(i)+" - tab = "+str(tab[i]))
        else:
            print("NO - i = "+str(i))
            e+=1

# Algorithmie Linéaire Double Tableau
def exempleAlgoLineaireDouble_ModelA():
    tab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i=1
    e=0
    while i < len(tab)-1 :
        while e < (i-1) :
            print("e = "+str(e)+" - i = "+str(i)+" - tabe/i = "+str(tab[i])+" - tab/e = "+str(tab[e]))
            if tab[i] == tab[e]:
                print("OK - i = "+str(i)+" - tab dans i = "+str(tab[i])+" - tab dans e = "+str(tab[e]))
            else :
                print("NO - i = null")
            e+=1
        i+=1

def exempleAlgoLineaireDouble_ModelB():
    tab1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    tab2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i=0
    while i<(len(tab1)-1) and i<(len(tab2)-1):
        if tab1[i]==i and tab2[i]==i:
            print("OK - i = "+str(i)+" - tab1 = "+str(tab1[i])+" - tab2 = "+str(tab2[i]))
        else:
            print("NO - i = "+str(i))
        i+=1