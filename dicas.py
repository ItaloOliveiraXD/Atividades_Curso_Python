import sys
# from gerar_cpf import gera_cpf
# from validar_cpf import valida_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow

import design


class App(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
