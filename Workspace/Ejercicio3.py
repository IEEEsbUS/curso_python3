#! /usr/bin/env python3
from tabulate import tabulate
from sys import argv

if len(argv)==2:
    print('Has metido correctamente el numero de parametros\n')
else:
    print('No has introducido correctamente los parametros\n')
    exit()


listaCompra = {}

nombreFichero = argv[1]

fichero = open(nombreFichero, 'r+')

for i in range (6):
    linea = fichero.readline()
    linea = linea.replace('\n', '')
    linea = linea.split(',')

    listaCompra.update({linea[0]:(int(linea[1]), float(linea[2]))})

fichero.close()

precioFinal = 0

for key in listaCompra.keys():
    cantidad = listaCompra.get(key)[0]
    precio = listaCompra.get(key)[1]
    preciFinal = precio + (cantidad * precio)

print (preciFinal)

listaNueva = []
for k, v in listaCompra.items():

    cantidad, precio = v

    listaNueva.append([k, cantidad, precio])


#print(tabulate(listaCompra.items(), headers = ["comidas", "cantidades"]))
print(tabulate(listaNueva, headers = ["comidas", "cantidades", "Precios"]))




#print(listaCompra)
