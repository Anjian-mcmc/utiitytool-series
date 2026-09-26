from random import *
seed(__import__('secrets').randbits(256))
if __name__ == '__main__':
    l = [1,23,324]
    shuffle(l)
    print(l)