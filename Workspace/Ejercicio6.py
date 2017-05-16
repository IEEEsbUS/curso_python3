#! /usr/bin/env python3

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# Declaramos la clase y hacemos que herede de QWidget
class Ejemplo(QMainWindow):

    # Llamamos al init de QWidget con el super()
    def __init__(self):
        super().__init__()
        self.initUI()

    # Aplicamos nuestras caracteristicas a la aplicación
    def initUI(self):
        self.setGeometry(600, 600, 600, 600)  # Este método junta el resize y el move (Eje x, eje y, anchura, altura)
        self.title = self.setWindowTitle('Ventana de cabesas')
        self.setWindowIcon(QIcon('icon.png'))  # Añadimos un icon a la ventana creada


        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton("¿Es un cabesa?", self)
        self.button.resize(160, 40)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.clicar)
        self.show()

    @pyqtSlot()
    def clicar(self):
        textboxValue = self.textbox.text()

        s1 = textboxValue
        s2 = 'Puchero'
        #set1 = (s1.split(' '))
        #set2 = (s2.split(' '))

        if s1 == s2:
            QMessageBox.question(self, textboxValue + "¡¡Es un gran cabeson!!", QMessageBox.Ok, QMessageBox.Ok)

        else:
            QMessageBox.question(self, textboxValue + "¡¡No es nada cabeson!!", QMessageBox.Ok, QMessageBox.Ok)


        #self.textbox.setText("")

app = QApplication(sys.argv)
ex = Ejemplo()
sys.exit(app.exec_())
