#! /usr/bin/env python3

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont, QIcon
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

        # Se declara la fuente que se va a usar tanto tipo como tamaño
        QToolTip.setFont(QFont('SansSerif', 15))

        self.setToolTip('Esto es una <b>PRUEBA</b> de como añadir un ToolTip')

        # Añadimos un boton
        btn = QPushButton('No pulsar', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        # Añadimos el tip del boton
        btn.setToolTip('Esto es un <b>BOTÓN</b>')

        # El boton tiene un tamaño establecido por su sizeHint()
        btn.resize(btn.sizeHint())

        # Indicamos la posicion del boton dentro de la ventana
        btn.move(50, 50)

        self.show()

app = QApplication(sys.argv)
ex = Ejemplo()
sys.exit(app.exec_())
