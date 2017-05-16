#! /usr/bin/env python3

# Cargamos el fichero en memoria

file_loaded = open('archivo_prueba.txt', 'a')
#La 'a' dice que continues por donde estabas leyendo en el archivo. Para leer y escribir poner 'r+'.

# Leemos el contenido completo

print(file_loaded.read())
#Podemos asi mismo guardarlo en archivos.

# Leemos unicamente la primera linea

print(file_loaded.readline())

# Escribimos al final del documento

file_loaded.write('Esto deberia escribirse en la ultima linea del documento')
#El write funciona

#Cerramos el fichero

file_loaded.close()