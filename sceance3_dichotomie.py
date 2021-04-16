def demoRechercheDichotomique():
    print("La recherche dichotomique :")
    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    debut = 0
    fin = 9  # -- n
    element = 5
    rechercheDichotomique(tab, debut, fin, element)

def rechercheDichotomique(tab, debut, fin, element):
    n=fin

    #calcul du pivot
    pivot = len(tab)/2

    if element == pivot :
        return True
    if debut == fin and pivot != element :
        return False
    if pivot < element :
        return rechercheDichotomique(tab, pivot+1, n, element)
    if pivot > element :
        return rechercheDichotomique(tab, 0, pivot-1, element)