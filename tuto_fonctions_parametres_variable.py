# Exemple de function avec des paramètres variables

def saluer(*args, **kwargs):
    return 'Bonjour ' + ', '.join(args) + ' ' + kwargs['nom']

# Exemple de générateur avec des paramètres variables
def demoGenerateur():
    while True:
        yield 1
def demoGenerateurStart():
    gen = demoGenerateur()
    print(gen.__next__())

def demoCountdown(start):
    while start >= 0:
        yield start
        start -= 1

def demoCountdownStart():
    start = 15
    print(demoCountdown(start))
    print('---')
    my_countdown = demoCountdown(start)
    print(next(my_countdown))
    print(next(my_countdown))
    print(next(my_countdown))
    print(next(my_countdown))
    print('---')
    for num in my_countdown:
        print(num)