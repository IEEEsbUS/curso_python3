#! /usr/bin/env python3

# Declaramos las variables

numero1 = 24
numero2 = 32

# Condicion if

if numero1 < numero2:
    numero3 = numero1 + numero2

# Condicion elif

if numero2 < numero1:
    print('Se imprime algo porque se cumple la condición.')
elif numero1 < numero2:
    print('Se imprime algo porque la condicion anterior no se cumple.')


# Condicion else

if numero2 < numero1:
    print('Se imprime algo porque se cumple la condición.')
elif numero1 == numero2:
    print('Se imprime algo porque la condicion anterior no se cumple.')
else:
    print('Se imprime algo porque ninguna de las condiciones anteriores se ha cumplido.')