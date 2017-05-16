#! /usr/bin/env python3
from tabulate import tabulate

# EJERCICIO2

# Con los datos del ejercicio anterior, vamos a sustituir en dict anterior, la cantidad por una tupla
# donde tengamos el la cantidad y el precio por unidad (cantidad, precio) y usaremos un bucle for para
# calcular el precio total de nuestra lista de la compra.


listaCompra = {"Manzanas": 2, "Caja de cereales": 1, "Caja de chele": 1, "Huevos": 12, "Bollos de pan": 3,
               "Botelline": 48}

listaPrecio = [0.20, 1.20, 0.40, 0.25, 0.15]
#print(tabulate(listaCompra.items(), headers=["comidas", "cantidades", "precios"]))

kek = zip(listaCompra.keys(), listaPrecio)

for comida, p in kek:
    #print(comida, cantidad, p)
    listaCompra.update({comida:(listaCompra.get(comida), p)})

    #lista_compra = {comida:(listaCompra.get(comida), p)}

#    print('\n', str(comida).ljust(15), '-->'.ljust(5), str(cantidad).ljust(5))
# Comando ljust(10) para ajustar el texto.


print (listaCompra)