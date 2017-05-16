#! /usr/bin/env python3

# Cargamos el fichero en memoria

file_loaded = open('archivo_prueba.txt', 'a')

# Leemos el contenido completo

print(file_loaded.read())

# Leemos unicamente la primera linea

print(file_loaded.readline())

# Escribimos al final del documento

file_loaded.write('Esto deberia escribirse en la ultima linea del documento')
