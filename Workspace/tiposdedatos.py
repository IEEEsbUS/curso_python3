#! /usr/bin/env python3
#Indica la version de Python que utiliza.



# Boolean

b = True
b2 = False

# Integer

i = 2
i.bit_length()
#Comprobar el tamanyo en bits del integer.


# Float

f = 2.5
f.is_integer()
#Preguntas si es un integer.


# String

s = "Hola!"
#Se puede utilizar comilla simple o doble, no hay una norma para utilizarlo.
s.isdecimal()
s.isdigit()
s.isalnum()
s.islower()
s.isupper()
s.isalpha()#Para saber si es una cadena contenida en el alfabeto.
#Metodos utilizados para string. Convierte el tipo de dato.

# Tuple

t = (s, i)#Devuelve el elemento i de la tupla s.
t[0]#Devuelve el elemento directo de la tupla.
t.count()


# Listas

l = []
l.count()
l.append()#Anyadir un elemento al final de la lista.
l.remove()
l.reverse()#Invertir el orden de la lista.
l.clear()
l.insert()#Insertar, machaca el elemento en la posicion.
#Las listas son arrays.


# dict

d = { "Key":2, "Hola":"Value"}#String relacionado con un integer y un string relacionado con otro string.
d.clear()
d.get()#Devuelve el valor/es asociado a una clave.
d.keys()#Lista con las claves.
d.values()#Lista con los valores.
d.setdefault()#Todas las claves que no tengan valor asociado, por defecto obtienen este valor.
d.update()#Le pasamos un diccionaro y nos lo une a otro.
#El set se declara igual que el diccionario pero se utilia poco.
set = {"key" "hola"}#Forma de declarase un set.

