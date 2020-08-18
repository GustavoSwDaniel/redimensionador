#pylint: disable = no-name-in-module
#pyuic5 design.ui -o design.py

import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class Redimensionar(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimencionar.clicked.connect(self.redimencionar)
        self.btnSalvar.clicked.connect(self.salvar)
    

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            '/home/lobo/Imagens/'
    )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImage.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.InputAltura.setText(str(self.original_img.height()))
    
    
    def redimencionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImage.setPixmap(self.nova_imagem)

        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.InputAltura.setText(str(self.nova_imagem.height()))


    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            '/home/lobo/Desktop/'
        )
        self.nova_imagem.save(imagem, 'PNG')



if __name__ == "__main__":
    qt = QApplication(sys.argv)
    redimensionar = Redimensionar()
    redimensionar.show()
    qt.exec_()