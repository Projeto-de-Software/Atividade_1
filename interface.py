# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from syntax_analisys import *
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnVizualizar = QtWidgets.QPushButton(self.groupBox_6)
        self.btnVizualizar.setMinimumSize(QtCore.QSize(120, 0))
        self.btnVizualizar.setObjectName("btnVizualizar")
        self.horizontalLayout.addWidget(self.btnVizualizar)

        self.btnSalvar = QtWidgets.QPushButton(self.groupBox_6)
        self.btnSalvar.setMinimumSize(QtCore.QSize(120, 0))
        self.btnSalvar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnSalvar.clicked.connect(self.btnSalvarClick)

        self.horizontalLayout.addWidget(self.btnSalvar)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_arquivo = QtWidgets.QLabel(self.groupBox_8)
        self.label_arquivo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_arquivo.setObjectName("label_arquivo")
        self.horizontalLayout_3.addWidget(self.label_arquivo)
        self.displayPath = QtWidgets.QLineEdit(self.groupBox_8)
        self.displayPath.setEnabled(False)
        self.displayPath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.displayPath.setObjectName("displayPath")
        self.horizontalLayout_3.addWidget(self.displayPath)

        self.btnProcurar = QtWidgets.QPushButton(self.groupBox_8)
        self.btnProcurar.setMinimumSize(QtCore.QSize(120, 0))
        self.btnProcurar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btnProcurar.setObjectName("btnProcurar")
        self.btnProcurar.clicked.connect(self.btnProcurarClick)

        self.horizontalLayout_3.addWidget(self.btnProcurar)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.displayTextAquivo = QtWidgets.QPlainTextEdit(self.groupBox)
        self.displayTextAquivo.setEnabled(False)
        self.displayTextAquivo.setObjectName("displayTextAquivo")
        self.gridLayout_2.addWidget(self.displayTextAquivo, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_4.addWidget(self.plainTextEdit_2, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelUrl = QtWidgets.QLabel(self.groupBox_9)
        self.labelUrl.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelUrl.setObjectName("labelUrl")
        self.horizontalLayout_4.addWidget(self.labelUrl)
        self.inputUrl = QtWidgets.QLineEdit(self.groupBox_9)
        self.inputUrl.setMaximumSize(QtCore.QSize(16777215, 30))
        self.inputUrl.setObjectName("inputUrl")
        self.horizontalLayout_4.addWidget(self.inputUrl)
        self.btnCarregarDadosUrl = QtWidgets.QPushButton(self.groupBox_9)
        self.btnCarregarDadosUrl.setMinimumSize(QtCore.QSize(120, 0))
        self.btnCarregarDadosUrl.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btnCarregarDadosUrl.setObjectName("btnCarregarDadosUrl")
        self.horizontalLayout_4.addWidget(self.btnCarregarDadosUrl)
        self.gridLayout_9.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnVizualizar.setText(_translate("MainWindow", "Vizualizar An??lise"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar An??lise"))
        self.groupBox.setTitle(_translate("MainWindow", "Texto"))
        self.label_arquivo.setText(_translate("MainWindow", "Arquivo:"))
        self.btnProcurar.setText(_translate("MainWindow", "Procurar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Arquivo"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Link do Wikipedia"))
        self.labelUrl.setText(_translate("MainWindow", "URL:"))
        self.btnCarregarDadosUrl.setText(_translate("MainWindow", "Carregar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "WEB"))


    def btnProcurarClick(self):
        file, check = QFileDialog.getOpenFileName(None, "Carregar arquivo",
                                                  "", "Text Files (*.txt)")
        if (check):
            self.displayPath.setText(file)
            fileText = open(file, "r", encoding="UTF-8")
            self.displayTextAquivo.setPlainText(fileText.read())
            fileText.close()

    def btnSalvarClick(self):
        try:
            a = ""
            if self.tab.isVisible():
                a = SyntaxAnalisys(self.displayTextAquivo.toPlainText())
            else:
                a = SyntaxAnalisys(self.plainTextEdit_2.toPlainText())

            a.analyze()

            arq = open('result.txt', 'w')

            arq.write("Verbos: " + str(a.verbos) + "\n")
            arq.write("Verbos Auxiliares: " + str(a.verbos_aux) + "\n")
            arq.write("Pronomes: " + str(a.pronomes) + "\n")
            arq.write("Substantivos Comuns: " + str(a.subst_comuns) + "\n")
            arq.write("Substantivos Pr??prios: " + str(a.subst_proprios) + "\n")
            arq.write("Conjun????es: " + str(a.conjuncoes) + "\n")
            arq.close()
            os.system("start result.txt")

        except Exception as e:
            self.alert(title="Erro", information="N??o foi poss??vel esta opera????o, por favor selecione um arquivo.",
                       detail=str(e))


    def alert(self, title, information, type='W', detail=None):
        msg = QMessageBox()

        if (type == "I"):
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.Warning)

        if (detail != None):
            msg.setDetailedText(detail)

        msg.setText(information)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())