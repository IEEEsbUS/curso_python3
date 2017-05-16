#! /usr/bin/env python3

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

# Declaramos la clase y hacemos que herede de QWidget
class Ejemplo(QWidget):

    # Llamamos al init de QWidget con el super()
    def __init__(self):
        super().__init__()
        self.initUI()

    # Aplicamos nuestras caracteristicas a la aplicación
    def initUI(self):

        # Caracteristicas de la ventana
        self.setGeometry(300, 300, 300, 300) # Este método junta el resize y el move (Eje x, eje y, anchura, altura)
        self.setWindowTitle('Ventana con icono de github')
        self.setWindowIcon(QIcon('github_icon.png')) # Añadimos un icon a la ventana creada
        self.show()

    def closeEvent(self, event):
        # Creamos el cuadro de pregunta, con question(self, 'Titulo de la ventana', 'Mensaje a mostrar', Respues 1 | Respuesta 2, Respuesta por defecto)
        reply = QMessageBox.question(self, 'Mensaje del sistema',
                                     "¿Esta seguro de que quieres cerrar la ventana?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        # Comprobamos cual es la respuesta dada
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)
ex = Ejemplo()
sys.exit(app.exec_())
