# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(436, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_gerar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gerar.sizePolicy().hasHeightForWidth())
        self.btn_gerar.setSizePolicy(sizePolicy)
        self.btn_gerar.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_gerar.setFont(font)
        self.btn_gerar.setObjectName("btn_gerar")
        self.gridLayout.addWidget(self.btn_gerar, 2, 0, 1, 1)
        self.btn_validar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_validar.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_validar.setFont(font)
        self.btn_validar.setObjectName("btn_validar")
        self.gridLayout.addWidget(self.btn_validar, 2, 1, 1, 1)
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.gridLayout.addWidget(self.label_titulo, 0, 0, 1, 2)
        self.input_msg = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_msg.sizePolicy().hasHeightForWidth())
        self.input_msg.setSizePolicy(sizePolicy)
        self.input_msg.setObjectName("input_msg")
        self.gridLayout.addWidget(self.input_msg, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador de CPF"))
        self.btn_gerar.setText(_translate("MainWindow", "Gerar"))
        self.btn_validar.setText(_translate("MainWindow", "Validar"))
        self.label_titulo.setText(_translate("MainWindow", "Gerador de CPF"))
