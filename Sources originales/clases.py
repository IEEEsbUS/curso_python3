#! /usr/bin/env python3

# Declaramos el inicio de la clase

class ejemplo(object):

# Definimos una función cualquiera dentro de la clase

    def funcion_ejemplo(self):
        self.numero = 5
        print(self.numero)

# Definimos __init__ para que se ejecute siempre que llamemos a la clase

    def __init__(self):
        print('Esto será lo primero que se muestre')
        self.funcion_ejemplo()
        print('Se imprime de nuevo el numero %s' % (self.numero))