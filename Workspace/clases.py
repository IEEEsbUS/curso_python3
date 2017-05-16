#! /usr/bin/env python3

# Declaramos el inicio de la clase

class ejemplo(object):

# Definimos una función cualquiera dentro de la clase
#Si estamos dentro de la clase, llamamos a "self" le indicamos que tiene acceso a todas las variables de la clase.

    def funcion_ejemplo(self):
        self.numero = 5
        print(self.numero)

# Definimos __init__ para que se ejecute siempre que llamemos a la clase

    def __init__(self):
        print('Esto será lo primero que se muestre')
        self.funcion_ejemplo()#LLamada a la funcion de la propia clase, si fuese otra clase pondriamos nombreclase.funcion.
        print('Se imprime de nuevo el numero %s' % (self.numero))

'''
Podemos usar en vez del init crearnos una llamada a un main.
    if __name__ == '__main__':
        funcion_ejemplo()
'''