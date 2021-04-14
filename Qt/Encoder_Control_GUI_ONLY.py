# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encoder_Control_GUI_ONLY.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tester(object):
    def setupUi(self, Tester):
        Tester.setObjectName("Tester")
        Tester.resize(592, 334)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/Cirris.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tester.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Tester)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RecordingEnco = QtWidgets.QSlider(self.groupBox_2)
        self.RecordingEnco.setOrientation(QtCore.Qt.Horizontal)
        self.RecordingEnco.setObjectName("RecordingEnco")
        self.verticalLayout_2.addWidget(self.RecordingEnco)
        self.RegisterEnco = QtWidgets.QCheckBox(self.groupBox_2)
        self.RegisterEnco.setObjectName("RegisterEnco")
        self.verticalLayout_2.addWidget(self.RegisterEnco)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ToConnectButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ToConnectButton.setObjectName("ToConnectButton")
        self.verticalLayout_3.addWidget(self.ToConnectButton)
        self.ToDisconnectButton = QtWidgets.QPushButton(self.groupBox_5)
        self.ToDisconnectButton.setObjectName("ToDisconnectButton")
        self.verticalLayout_3.addWidget(self.ToDisconnectButton)
        self.DisplayPlotButton = QtWidgets.QPushButton(self.groupBox_5)
        self.DisplayPlotButton.setObjectName("DisplayPlotButton")
        self.verticalLayout_3.addWidget(self.DisplayPlotButton)
        self.DisplayData_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.DisplayData_2.setObjectName("DisplayData_2")
        self.verticalLayout_3.addWidget(self.DisplayData_2)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.textEditDirectory = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEditDirectory.setObjectName("textEditDirectory")
        self.verticalLayout_8.addWidget(self.textEditDirectory)
        self.DirectoryConfirmB = QtWidgets.QPushButton(self.groupBox_4)
        self.DirectoryConfirmB.setObjectName("DirectoryConfirmB")
        self.verticalLayout_8.addWidget(self.DirectoryConfirmB)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.textEditFile = QtWidgets.QTextEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditFile.sizePolicy().hasHeightForWidth())
        self.textEditFile.setSizePolicy(sizePolicy)
        self.textEditFile.setObjectName("textEditFile")
        self.verticalLayout_4.addWidget(self.textEditFile)
        self.FileConfirmButton = QtWidgets.QPushButton(self.groupBox_4)
        self.FileConfirmButton.setObjectName("FileConfirmButton")
        self.verticalLayout_4.addWidget(self.FileConfirmButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_9.addWidget(self.spinBox)
        self.DataIntervalButton = QtWidgets.QPushButton(self.groupBox_4)
        self.DataIntervalButton.setObjectName("DataIntervalButton")
        self.verticalLayout_9.addWidget(self.DataIntervalButton)
        self.gridLayout.addLayout(self.verticalLayout_9, 1, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout.addLayout(self.verticalLayout_10, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 3)
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout_2.addWidget(self.CloseButton, 1, 3, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdTimeRecording = QtWidgets.QLCDNumber(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdTimeRecording.sizePolicy().hasHeightForWidth())
        self.lcdTimeRecording.setSizePolicy(sizePolicy)
        self.lcdTimeRecording.setObjectName("lcdTimeRecording")
        self.verticalLayout.addWidget(self.lcdTimeRecording)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lcdPositionChange = QtWidgets.QLCDNumber(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdPositionChange.sizePolicy().hasHeightForWidth())
        self.lcdPositionChange.setSizePolicy(sizePolicy)
        self.lcdPositionChange.setObjectName("lcdPositionChange")
        self.verticalLayout.addWidget(self.lcdPositionChange)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lcdTimeChange = QtWidgets.QLCDNumber(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdTimeChange.sizePolicy().hasHeightForWidth())
        self.lcdTimeChange.setSizePolicy(sizePolicy)
        self.lcdTimeChange.setObjectName("lcdTimeChange")
        self.verticalLayout.addWidget(self.lcdTimeChange)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lcdDistance = QtWidgets.QLCDNumber(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdDistance.sizePolicy().hasHeightForWidth())
        self.lcdDistance.setSizePolicy(sizePolicy)
        self.lcdDistance.setObjectName("lcdDistance")
        self.verticalLayout.addWidget(self.lcdDistance)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        Tester.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tester)
        QtCore.QMetaObject.connectSlotsByName(Tester)

    def retranslateUi(self, Tester):
        _translate = QtCore.QCoreApplication.translate
        Tester.setWindowTitle(_translate("Tester", "Interface de contrôle"))
        self.groupBox_2.setTitle(_translate("Tester", "Encoder"))
        self.RegisterEnco.setText(_translate("Tester", "Enregistrement"))
        self.groupBox_5.setTitle(_translate("Tester", "Connectivité"))
        self.ToConnectButton.setText(_translate("Tester", "connexion"))
        self.ToDisconnectButton.setText(_translate("Tester", "Déconnexion"))
        self.DisplayPlotButton.setText(_translate("Tester", "graphique"))
        self.DisplayData_2.setText(_translate("Tester", "reset distance"))
        self.label_2.setText(_translate("Tester", "Dossier"))
        self.DirectoryConfirmB.setText(_translate("Tester", "Confirmer"))
        self.label.setText(_translate("Tester", "Fichier"))
        self.FileConfirmButton.setText(_translate("Tester", "Confirmer"))
        self.label_7.setText(_translate("Tester", "Data Interval"))
        self.DataIntervalButton.setText(_translate("Tester", "Confirmer"))
        self.label_8.setText(_translate("Tester", "https://github.com/WilliamBonilla62/GUIPythonEncodeur"))
        self.CloseButton.setText(_translate("Tester", "Fermer"))
        self.groupBox_3.setTitle(_translate("Tester", "Afficher données"))
        self.label_3.setText(_translate("Tester", "Time recording [s]"))
        self.label_4.setText(_translate("Tester", "Position Change"))
        self.label_5.setText(_translate("Tester", "Time change [ms]"))
        self.label_9.setText(_translate("Tester", "Distance [dm]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tester = QtWidgets.QMainWindow()
    ui = Ui_Tester()
    ui.setupUi(Tester)
    Tester.show()
    sys.exit(app.exec_())