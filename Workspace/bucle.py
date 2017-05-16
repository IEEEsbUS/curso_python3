#! /usr/bin/env python3

# Declaramos las variables con las que vamos a trabajar

n = 30
i = 0

lista = ['Juan', 'Antonio', 'Perico', 'Amancio', 'Jose Manuel']

# While

while i < n:
    print('El numero i es menor que n')
    i += 1  # Actualizamos la condicion para no mantenernos en un bucle infinito

# For con integer

for j in range(40):        # j obtendrá los valores [0, 40)
    print(j)

# For con elementos de una lista

for nombre in lista:
    print(nombre)