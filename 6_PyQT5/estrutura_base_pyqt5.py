import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QWidget, QGridLayout


def teste():
    print('Está funcionando!')


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()  # Centro_Widget
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto botão')
        # Usando o css no botão
        self.btn.setStyleSheet('font-size: 20px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        # Adicionando uma funcionalidade para o botão
        self.btn.clicked.connect(teste)

        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
