#! /usr/bin/env python3

# Declaramos una función

def ejemplo(num, num2):
    suma = num + num2
    print('La suma total es de $s' % (suma))

    mult = num * num2
    print('La multiplicación de ambos numeros es %s' % (mult))

def ejemplo_return(num, num2):
    suma = num + num2
    return suma


ejemplo(4, 10)

print('Imprimimos el numero por llamada directa al metodo %s' % (ejemplo_return(4, 10)))

# No podemos hacer llamada a variables declaradas dentro de la funcion desde fuera
# Sin embargo si podemos usar variables declaradas fuera de la función dentro de ella.

# print(suma)

