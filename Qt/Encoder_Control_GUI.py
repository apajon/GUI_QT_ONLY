# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encoder_Control_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tester(object):
    def setupUi(self, Tester):
        Tester.setObjectName("Tester")
        Tester.resize(673, 541)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/Cirris.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tester.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Tester)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 0, 191, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.RecordingEnco = QtWidgets.QSlider(self.groupBox_2)
        self.RecordingEnco.setGeometry(QtCore.QRect(10, 30, 160, 16))
        self.RecordingEnco.setOrientation(QtCore.Qt.Horizontal)
        self.RecordingEnco.setObjectName("RecordingEnco")
        self.RegisterEnco = QtWidgets.QCheckBox(self.groupBox_2)
        self.RegisterEnco.setGeometry(QtCore.QRect(10, 50, 92, 23))
        self.RegisterEnco.setObjectName("RegisterEnco")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(580, 470, 89, 25))
        self.CloseButton.setObjectName("CloseButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 181, 391))
        self.groupBox_3.setObjectName("groupBox_3")
        self.DisplayPlotButton = QtWidgets.QPushButton(self.groupBox_3)
        self.DisplayPlotButton.setGeometry(QtCore.QRect(10, 350, 161, 25))
        self.DisplayPlotButton.setObjectName("DisplayPlotButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 40, 141, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 161, 17))
        self.label_3.setObjectName("label_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(10, 110, 141, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 161, 17))
        self.label_4.setObjectName("label_4")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber_3.setGeometry(QtCore.QRect(10, 180, 141, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber_4.setGeometry(QtCore.QRect(10, 250, 141, 51))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 161, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 161, 17))
        self.label_6.setObjectName("label_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 0, 271, 401))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 251, 70))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label.setObjectName("label")
        self.FileConfirmButton = QtWidgets.QPushButton(self.groupBox_4)
        self.FileConfirmButton.setGeometry(QtCore.QRect(10, 130, 251, 25))
        self.FileConfirmButton.setObjectName("FileConfirmButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 200, 251, 70))
        self.textEdit_2.setObjectName("textEdit_2")
        self.DirectoryConfirmB = QtWidgets.QPushButton(self.groupBox_4)
        self.DirectoryConfirmB.setGeometry(QtCore.QRect(10, 280, 251, 25))
        self.DirectoryConfirmB.setObjectName("DirectoryConfirmB")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 67, 17))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setGeometry(QtCore.QRect(10, 330, 251, 26))
        self.spinBox.setObjectName("spinBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 131, 17))
        self.label_7.setObjectName("label_7")
        self.DataIntervalButton = QtWidgets.QPushButton(self.groupBox_4)
        self.DataIntervalButton.setGeometry(QtCore.QRect(10, 360, 251, 25))
        self.DataIntervalButton.setObjectName("DataIntervalButton")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(200, 100, 191, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.ToConnectButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ToConnectButton.setGeometry(QtCore.QRect(10, 30, 171, 31))
        self.ToConnectButton.setObjectName("ToConnectButton")
        self.ToDisconnectButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ToDisconnectButton.setGeometry(QtCore.QRect(10, 70, 171, 31))
        self.ToDisconnectButton.setObjectName("ToDisconnectButton")
        Tester.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tester)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 22))
        self.menubar.setObjectName("menubar")
        Tester.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tester)
        self.statusbar.setObjectName("statusbar")
        Tester.setStatusBar(self.statusbar)

        self.retranslateUi(Tester)
        QtCore.QMetaObject.connectSlotsByName(Tester)

    def retranslateUi(self, Tester):
        _translate = QtCore.QCoreApplication.translate
        Tester.setWindowTitle(_translate("Tester", "Interface de contrôle"))
        self.groupBox_2.setTitle(_translate("Tester", "Encoder"))
        self.RegisterEnco.setText(_translate("Tester", "Enrigistrement"))
        self.CloseButton.setText(_translate("Tester", "Fermer"))
        self.groupBox_3.setTitle(_translate("Tester", "Afficher données"))
        self.DisplayPlotButton.setText(_translate("Tester", "Graphique de donnée"))
        self.label_3.setText(_translate("Tester", "Time recording"))
        self.label_4.setText(_translate("Tester", "Position Change"))
        self.label_5.setText(_translate("Tester", "Time change"))
        self.label_6.setText(_translate("Tester", "Index Triggered"))
        self.groupBox_4.setTitle(_translate("Tester", "Fichier"))
        self.label.setText(_translate("Tester", "Fichier"))
        self.FileConfirmButton.setText(_translate("Tester", "Confirmer"))
        self.DirectoryConfirmB.setText(_translate("Tester", "Confirmer"))
        self.label_2.setText(_translate("Tester", "Dossier"))
        self.label_7.setText(_translate("Tester", "Data Interval"))
        self.DataIntervalButton.setText(_translate("Tester", "Confirmer"))
        self.groupBox_5.setTitle(_translate("Tester", "Connectivité"))
        self.ToConnectButton.setText(_translate("Tester", "Lancer connexion"))
        self.ToDisconnectButton.setText(_translate("Tester", "Déconnexion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tester = QtWidgets.QMainWindow()
    ui = Ui_Tester()
    ui.setupUi(Tester)
    Tester.show()
    sys.exit(app.exec_())