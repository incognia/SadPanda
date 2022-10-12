# Se ejecuta en Python 2

import random

n = random.randint(1,99)
guess = int(raw_input("Ingresa un entero entre 1 y 99: "))
while n != "guess":
    print
    if guess < n:
        print "muy bajo"
        guess = int(raw_input("Ingresa un entero entre 1 y 99: "))
    elif guess > n:
        print "muy alto"
        guess = int(raw_input("Ingresa un entero entre 1 y 99: "))
    else:
        print "adivinaste"
        break
    print
