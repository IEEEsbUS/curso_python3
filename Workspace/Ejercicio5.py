#! /usr/bin/env python3

from tabulate import tabulate
from sys import argv

class lista_compra(object):

    def check (self):
        if len(argv)==2:
            print('Has metido correctamente el numero de parametros\n')
        else:
            print('No has introducido correctamente los parametros\n')
            exit()

    def parser(self):
        self.listaCompra = {}

        self.nombreFichero = "lista_compra.txt"

        try:
            fichero = open(self.nombreFichero, 'r+')
        except:
            print("Se ha producido un error")
            exit()

        for i in range (6):
            linea = fichero.readline().replace('\n', '').split(',')

            self.listaCompra.update({linea[0]:(int(linea[1]), float(linea[2]))})

        fichero.close()

    def calcula_precio (self, lista):
        precio_temp = 0

        for key in lista.keys():
            cantidad = lista.get(key)[0]
            precio = lista.get(key)[1]
            precio_temp += (cantidad * precio)

        return precio_temp

    def imprime_cosas (self):
        listaNueva = []
        for k, v in self.listaCompra.items():

            cantidad, precio = v

            listaNueva.append([k, cantidad, precio])

        print(tabulate(listaNueva, headers = ["comidas", "cantidades", "Precios"]))

        print ("\nEl precio final de nuestra lista de la compra es %s €\n" % round(self.calcula_precio(self.listaCompra), 3))


    def __init__(self):
        self.check()
        self.parser()
        self.calcula_precio(self.listaCompra)
        self.imprime_cosas()


lista_compra()