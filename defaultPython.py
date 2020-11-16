import sys

def print_hi(name):
    print(f'Hi, {name}')

def pythonVersion():
    if not sys.version_info.major == 3 and sys.version_info.minor >= 6:
        print("Python 3.6 or higher is required.")
    else:
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    #sys.exit(1)