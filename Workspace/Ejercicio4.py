#! /usr/bin/env python3

#Las funciones privadas se definen como "__nombre__".
#La funcion "__init__" se ejecuta automaticamente.
#Con return la funcion devuelve un dato.

from tabulate import tabulate

listaCompra = {}

nombreFichero = "lista_compra.txt"

fichero = open(nombreFichero, 'r+')

for i in range (6):
    linea = fichero.readline()
    linea = linea.replace('\n', '')
    linea = linea.split(',')

    listaCompra.update({linea[0]:(int(linea[1]), float(linea[2]))})

fichero.close()

def calculaPrecio (lista):
    precio_temp = 0

    for key in lista.keys():
        cantidad = lista.get(key)[0]
        precio = lista.get(key)[1]
        precio_temp += (cantidad * precio)

    return precio_temp

listaNueva = []
for k, v in listaCompra.items():

    cantidad, precio = v

    listaNueva.append([k, cantidad, precio])

print(tabulate(listaNueva, headers = ["comidas", "cantidades", "Precios"]))

print ("\nEl precio final de nuestra lista de la compra es %s €\n" % round(calculaPrecio(listaCompra), 3))
