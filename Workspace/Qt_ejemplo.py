#! /usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Iniciamos la Qt
app = QApplication(sys.argv)

# Iniciamos la ventana
w = QWidget()

# Cambia el tamaño de la ventana
w.resize(600, 150) # Anchura, Altura en píxeles

w.move(300, 300) # Posicion de la ventana, Eje x, Eje y

# Cambia el nombre de la ventana
w.setWindowTitle('Ventanita de ejemplo')

# Muestra la ventana
w.show()

# Finaliza la aplicacion
sys.exit(app.exec_())