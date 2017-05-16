#! /usr/bin/env python3

# Usamos unicamente import e importamos el módulo math

import math

# Usamos from para importar unicamente argv del modulo sys

from sys import argv

# Como math lo hemos importado con import tenemos que llamar antes al modulo

raiz_2 = math.sqrt(2)
print('La raiz de 2 es %s' % (raiz_2))

# Como argv lo hemos importado usando from, no debemos llamar al nombre del modulo antes de la función

if len(argv) == 1:
    print('No se ha introducido ningún parámetro')
else:
    print('El primer parámetro introducido es: %s' % (argv[1]))