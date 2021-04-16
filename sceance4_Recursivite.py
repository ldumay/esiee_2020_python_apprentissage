def recursivite():
    print("Les suites - La récursivité")
    suite = [1,3,5,7,9,11,13,15]
    premierTerme = 1
    raison = 2
    rechercheTerme = 2

    # u0 = 1
    # uN = u0+ r*n
    # uN = premierTerme + raison * rechercheTerme

    for i in range(premierTerme,len(suite)):
        if i == premierTerme:
            print("u"+str(i)+"="+str(i))
        else:
            uN = premierTerme + raison * i
            print("u"+str(i)+"="+str(uN))