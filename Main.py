# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import pyroomacoustics as pra
from pyroomacoustics.doa import circ_dist
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 557)
        MainWindow.setFixedSize(780,557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QMessageBox.Warning)
        self.error_dialog.setText("Error")
        self.error_dialog.setWindowTitle("Error")
        self.error_dialog.setInformativeText("Please fill all the parameters!")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 191))
        self.groupBox.setObjectName("groupBox")
        self.Y_value_2 = QtWidgets.QLineEdit(self.groupBox)
        self.Y_value_2.setGeometry(QtCore.QRect(230, 60, 41, 20))
        self.Y_value_2.setObjectName("Y_value_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 20))
        self.label.setToolTip("")
        self.label.setStatusTip("")
        self.label.setWhatsThis("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 131, 20))
        self.label_3.setObjectName("label_3")
        self.X_value = QtWidgets.QLineEdit(self.groupBox)
        self.X_value.setGeometry(QtCore.QRect(170, 30, 41, 20))
        self.X_value.setObjectName("X_value")
        self.X_value_2 = QtWidgets.QLineEdit(self.groupBox)
        self.X_value_2.setGeometry(QtCore.QRect(170, 60, 41, 20))
        self.X_value_2.setObjectName("X_value_2")
        self.Y_value = QtWidgets.QLineEdit(self.groupBox)
        self.Y_value.setGeometry(QtCore.QRect(230, 30, 41, 20))
        self.Y_value.setObjectName("Y_value")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(220, 60, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 20, 20))
        self.label_2.setObjectName("label_2")
        self.Temperature = QtWidgets.QLineEdit(self.groupBox)
        self.Temperature.setEnabled(False)
        self.Temperature.setGeometry(QtCore.QRect(170, 90, 41, 20))
        self.Temperature.setObjectName("Temperature")
        self.Humidity = QtWidgets.QLineEdit(self.groupBox)
        self.Humidity.setEnabled(False)
        self.Humidity.setGeometry(QtCore.QRect(170, 120, 41, 20))
        self.Humidity.setText("")
        self.Humidity.setObjectName("Humidity")
        self.Air = QtWidgets.QLineEdit(self.groupBox)
        self.Air.setEnabled(False)
        self.Air.setGeometry(QtCore.QRect(170, 150, 41, 20))
        self.Air.setText("")
        self.Air.setObjectName("Air")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 90, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 120, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 150, 101, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(280, 30, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(280, 60, 47, 13))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 391, 232))
        self.groupBox_2.setObjectName("groupBox_2")
        self.freqs = QtWidgets.QLineEdit(self.groupBox_2)
        self.freqs.setGeometry(QtCore.QRect(170, 180, 101, 20))
        self.freqs.setText("")
        self.freqs.setObjectName("freqs")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 90, 131, 20))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(220, 90, 20, 20))
        self.label_11.setObjectName("label_11")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 60, 131, 20))
        self.label_5.setObjectName("label_5")
        self.number = QtWidgets.QLineEdit(self.groupBox_2)
        self.number.setGeometry(QtCore.QRect(170, 60, 41, 20))
        self.number.setObjectName("number")
        self.c_x = QtWidgets.QLineEdit(self.groupBox_2)
        self.c_x.setGeometry(QtCore.QRect(170, 90, 41, 20))
        self.c_x.setObjectName("c_x")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 131, 20))
        self.label_6.setObjectName("label_6")
        self.circular = QtWidgets.QRadioButton(self.groupBox_2)
        self.circular.setGeometry(QtCore.QRect(30, 30, 101, 17))
        self.circular.setObjectName("circular")
        self.angle = QtWidgets.QLineEdit(self.groupBox_2)
        self.angle.setGeometry(QtCore.QRect(170, 150, 41, 20))
        self.angle.setObjectName("angle")
        self.inter = QtWidgets.QLineEdit(self.groupBox_2)
        self.inter.setGeometry(QtCore.QRect(170, 120, 41, 20))
        self.inter.setObjectName("inter")
        self.c_y = QtWidgets.QLineEdit(self.groupBox_2)
        self.c_y.setGeometry(QtCore.QRect(230, 90, 41, 20))
        self.c_y.setObjectName("c_y")
        self.Linear = QtWidgets.QRadioButton(self.groupBox_2)
        self.Linear.setGeometry(QtCore.QRect(150, 30, 82, 17))
        self.Linear.setChecked(True)
        self.Linear.setObjectName("Linear")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(30, 150, 131, 20))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(30, 180, 131, 20))
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(280, 90, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(220, 120, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(220, 150, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(280, 170, 111, 31))
        self.label_16.setScaledContents(False)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.simulate1 = QtWidgets.QPushButton(self.tab)
        self.simulate1.setGeometry(QtCore.QRect(210, 490, 151, 23))
        self.simulate1.setObjectName("simulate1")
        self.save1 = QtWidgets.QPushButton(self.tab)
        self.save1.setGeometry(QtCore.QRect(380, 490, 151, 23))
        self.save1.setObjectName("save1")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(410, 30, 351, 401))
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 341, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(30, 30, 51, 20))
        self.label_17.setObjectName("label_17")
        self.Azimuth = QtWidgets.QLineEdit(self.groupBox_3)
        self.Azimuth.setGeometry(QtCore.QRect(180, 30, 41, 20))
        self.Azimuth.setText("")
        self.Azimuth.setObjectName("Azimuth")
        self.Distance = QtWidgets.QLineEdit(self.groupBox_3)
        self.Distance.setGeometry(QtCore.QRect(180, 60, 41, 20))
        self.Distance.setText("")
        self.Distance.setObjectName("Distance")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(30, 60, 51, 20))
        self.label_18.setObjectName("label_18")
        self.label_45 = QtWidgets.QLabel(self.groupBox_3)
        self.label_45.setGeometry(QtCore.QRect(230, 30, 47, 13))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_3)
        self.label_46.setGeometry(QtCore.QRect(230, 60, 47, 13))
        self.label_46.setObjectName("label_46")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 130, 341, 181))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(30, 30, 131, 20))
        self.label_19.setObjectName("label_19")
        self.SNR = QtWidgets.QLineEdit(self.groupBox_4)
        self.SNR.setGeometry(QtCore.QRect(180, 30, 41, 20))
        self.SNR.setText("")
        self.SNR.setObjectName("SNR")
        self.Sound = QtWidgets.QLineEdit(self.groupBox_4)
        self.Sound.setGeometry(QtCore.QRect(180, 60, 41, 20))
        self.Sound.setObjectName("Sound")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(30, 60, 111, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(30, 90, 111, 20))
        self.label_21.setObjectName("label_21")
        self.fs = QtWidgets.QLineEdit(self.groupBox_4)
        self.fs.setGeometry(QtCore.QRect(180, 90, 41, 20))
        self.fs.setText("")
        self.fs.setObjectName("fs")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(30, 120, 111, 20))
        self.label_22.setObjectName("label_22")
        self.ffts = QtWidgets.QLineEdit(self.groupBox_4)
        self.ffts.setGeometry(QtCore.QRect(180, 120, 41, 20))
        self.ffts.setObjectName("ffts")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(30, 150, 111, 20))
        self.label_23.setObjectName("label_23")
        self.minb = QtWidgets.QLineEdit(self.groupBox_4)
        self.minb.setGeometry(QtCore.QRect(180, 150, 41, 20))
        self.minb.setText("")
        self.minb.setObjectName("minb")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(160, 150, 21, 20))
        self.label_24.setObjectName("label_24")
        self.maxb = QtWidgets.QLineEdit(self.groupBox_4)
        self.maxb.setGeometry(QtCore.QRect(260, 150, 41, 20))
        self.maxb.setText("")
        self.maxb.setObjectName("maxb")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(240, 150, 21, 20))
        self.label_25.setObjectName("label_25")
        self.label_47 = QtWidgets.QLabel(self.groupBox_4)
        self.label_47.setGeometry(QtCore.QRect(230, 90, 47, 13))
        self.label_47.setObjectName("label_47")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 320, 341, 161))
        self.groupBox_5.setObjectName("groupBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 70, 91, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.Air_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.Air_2.setEnabled(False)
        self.Air_2.setGeometry(QtCore.QRect(170, 130, 41, 20))
        self.Air_2.setText("")
        self.Air_2.setObjectName("Air_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_5.setGeometry(QtCore.QRect(30, 130, 101, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.Humidity_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.Humidity_2.setEnabled(False)
        self.Humidity_2.setGeometry(QtCore.QRect(170, 100, 41, 20))
        self.Humidity_2.setText("")
        self.Humidity_2.setObjectName("Humidity_2")
        self.Temperature_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.Temperature_2.setEnabled(False)
        self.Temperature_2.setGeometry(QtCore.QRect(170, 70, 41, 20))
        self.Temperature_2.setObjectName("Temperature_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 100, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        self.label_35.setGeometry(QtCore.QRect(280, 40, 47, 13))
        self.label_35.setObjectName("label_35")
        self.r_y = QtWidgets.QLineEdit(self.groupBox_5)
        self.r_y.setGeometry(QtCore.QRect(230, 40, 41, 20))
        self.r_y.setObjectName("r_y")
        self.r_x = QtWidgets.QLineEdit(self.groupBox_5)
        self.r_x.setGeometry(QtCore.QRect(170, 40, 41, 20))
        self.r_x.setObjectName("r_x")
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        self.label_33.setGeometry(QtCore.QRect(220, 40, 20, 20))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setGeometry(QtCore.QRect(30, 40, 131, 20))
        self.label_34.setToolTip("")
        self.label_34.setStatusTip("")
        self.label_34.setWhatsThis("")
        self.label_34.setObjectName("label_34")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(380, 20, 391, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_38 = QtWidgets.QLabel(self.groupBox_6)
        self.label_38.setGeometry(QtCore.QRect(30, 30, 131, 20))
        self.label_38.setObjectName("label_38")
        self.number_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.number_2.setGeometry(QtCore.QRect(170, 30, 41, 20))
        self.number_2.setObjectName("number_2")
        self.label_39 = QtWidgets.QLabel(self.groupBox_6)
        self.label_39.setGeometry(QtCore.QRect(30, 60, 131, 20))
        self.label_39.setObjectName("label_39")
        self.angle_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.angle_2.setGeometry(QtCore.QRect(170, 90, 41, 20))
        self.angle_2.setObjectName("angle_2")
        self.inter_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.inter_2.setGeometry(QtCore.QRect(170, 60, 41, 20))
        self.inter_2.setObjectName("inter_2")
        self.label_40 = QtWidgets.QLabel(self.groupBox_6)
        self.label_40.setGeometry(QtCore.QRect(30, 90, 131, 20))
        self.label_40.setObjectName("label_40")
        self.label_43 = QtWidgets.QLabel(self.groupBox_6)
        self.label_43.setGeometry(QtCore.QRect(220, 60, 47, 13))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_6)
        self.label_44.setGeometry(QtCore.QRect(220, 90, 47, 13))
        self.label_44.setObjectName("label_44")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(380, 150, 391, 251))
        self.groupBox_7.setObjectName("groupBox_7")
        self.music = QtWidgets.QCheckBox(self.groupBox_7)
        self.music.setGeometry(QtCore.QRect(30, 30, 70, 17))
        self.music.setChecked(True)
        self.music.setObjectName("music")
        self.srp = QtWidgets.QCheckBox(self.groupBox_7)
        self.srp.setGeometry(QtCore.QRect(30, 70, 70, 17))
        self.srp.setObjectName("srp")
        self.cssm = QtWidgets.QCheckBox(self.groupBox_7)
        self.cssm.setGeometry(QtCore.QRect(30, 110, 70, 17))
        self.cssm.setObjectName("cssm")
        self.waves = QtWidgets.QCheckBox(self.groupBox_7)
        self.waves.setGeometry(QtCore.QRect(30, 150, 70, 17))
        self.waves.setObjectName("waves")
        self.tops = QtWidgets.QCheckBox(self.groupBox_7)
        self.tops.setGeometry(QtCore.QRect(30, 190, 70, 17))
        self.tops.setObjectName("tops")
        self.label_36 = QtWidgets.QLabel(self.groupBox_7)
        self.label_36.setGeometry(QtCore.QRect(110, 30, 271, 31))
        self.label_36.setScaledContents(False)
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_7)
        self.label_37.setGeometry(QtCore.QRect(110, 70, 271, 31))
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.label_41 = QtWidgets.QLabel(self.groupBox_7)
        self.label_41.setGeometry(QtCore.QRect(110, 110, 271, 31))
        self.label_41.setWordWrap(True)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_7)
        self.label_42.setGeometry(QtCore.QRect(110, 150, 271, 31))
        self.label_42.setWordWrap(True)
        self.label_42.setObjectName("label_42")
        self.label_48 = QtWidgets.QLabel(self.groupBox_7)
        self.label_48.setGeometry(QtCore.QRect(110, 180, 271, 31))
        self.label_48.setWordWrap(True)
        self.label_48.setObjectName("label_48")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setGeometry(QtCore.QRect(380, 410, 391, 71))
        self.groupBox_8.setObjectName("groupBox_8")
        self.angle_3 = QtWidgets.QLineEdit(self.groupBox_8)
        self.angle_3.setGeometry(QtCore.QRect(170, 90, 41, 20))
        self.angle_3.setObjectName("angle_3")
        self.label_52 = QtWidgets.QLabel(self.groupBox_8)
        self.label_52.setGeometry(QtCore.QRect(30, 90, 131, 20))
        self.label_52.setObjectName("label_52")
        self.label_54 = QtWidgets.QLabel(self.groupBox_8)
        self.label_54.setGeometry(QtCore.QRect(220, 90, 47, 13))
        self.label_54.setObjectName("label_54")
        self.label_50 = QtWidgets.QLabel(self.groupBox_8)
        self.label_50.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_8)
        self.label_51.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.label_51.setObjectName("label_51")
        self.label_53 = QtWidgets.QLabel(self.groupBox_8)
        self.label_53.setGeometry(QtCore.QRect(110, 10, 47, 13))
        self.label_53.setObjectName("label_53")
        self.label_55 = QtWidgets.QLabel(self.groupBox_8)
        self.label_55.setGeometry(QtCore.QRect(150, 10, 47, 13))
        self.label_55.setObjectName("label_55")
        self.label_57 = QtWidgets.QLabel(self.groupBox_8)
        self.label_57.setGeometry(QtCore.QRect(250, 10, 47, 13))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_8)
        self.label_58.setGeometry(QtCore.QRect(300, 10, 47, 13))
        self.label_58.setObjectName("label_58")
        self.label_60 = QtWidgets.QLabel(self.groupBox_8)
        self.label_60.setGeometry(QtCore.QRect(210, 10, 47, 13))
        self.label_60.setObjectName("label_60")
        self.label_56 = QtWidgets.QLabel(self.groupBox_8)
        self.label_56.setGeometry(QtCore.QRect(110, 30, 31, 16))
        self.label_56.setScaledContents(False)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.label_61 = QtWidgets.QLabel(self.groupBox_8)
        self.label_61.setGeometry(QtCore.QRect(160, 30, 31, 16))
        self.label_61.setScaledContents(False)
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.groupBox_8)
        self.label_62.setGeometry(QtCore.QRect(210, 30, 31, 16))
        self.label_62.setScaledContents(False)
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.groupBox_8)
        self.label_63.setGeometry(QtCore.QRect(250, 30, 31, 16))
        self.label_63.setScaledContents(False)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.groupBox_8)
        self.label_64.setGeometry(QtCore.QRect(300, 30, 31, 16))
        self.label_64.setScaledContents(False)
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.label_66 = QtWidgets.QLabel(self.groupBox_8)
        self.label_66.setGeometry(QtCore.QRect(110, 50, 31, 16))
        self.label_66.setScaledContents(False)
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.groupBox_8)
        self.label_67.setGeometry(QtCore.QRect(160, 50, 31, 16))
        self.label_67.setScaledContents(False)
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.groupBox_8)
        self.label_68.setGeometry(QtCore.QRect(210, 50, 31, 16))
        self.label_68.setScaledContents(False)
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_8)
        self.label_69.setGeometry(QtCore.QRect(250, 50, 31, 16))
        self.label_69.setScaledContents(False)
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.groupBox_8)
        self.label_70.setGeometry(QtCore.QRect(300, 50, 31, 16))
        self.label_70.setScaledContents(False)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.simulate2 = QtWidgets.QPushButton(self.tab_2)
        self.simulate2.setGeometry(QtCore.QRect(210, 490, 151, 23))
        self.simulate2.setObjectName("simulate2")
        self.save2 = QtWidgets.QPushButton(self.tab_2)
        self.save2.setGeometry(QtCore.QRect(380, 490, 151, 23))
        self.save2.setObjectName("save2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beamforming & DOA"))
        self.groupBox.setTitle(_translate("MainWindow", "Room Parameters"))
        self.label.setText(_translate("MainWindow", "Room Size:                       X"))
        self.label_3.setText(_translate("MainWindow", "Source Position:               X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.label_2.setText(_translate("MainWindow", "Y"))
        self.checkBox.setText(_translate("MainWindow", "Tempurature"))
        self.checkBox_2.setText(_translate("MainWindow", "Humidity"))
        self.checkBox_3.setText(_translate("MainWindow", "Air Absorption"))
        self.label_10.setText(_translate("MainWindow", "Meters"))
        self.label_12.setText(_translate("MainWindow", "Meters"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Antennas Parameters"))
        self.label_8.setText(_translate("MainWindow", "Center:                             X"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "Number of Antenna: "))
        self.label_6.setText(_translate("MainWindow", "Inter Antenna Distance:"))
        self.circular.setText(_translate("MainWindow", "Circular Array"))
        self.Linear.setText(_translate("MainWindow", "Linear Array"))
        self.label_7.setText(_translate("MainWindow", "Angle: "))
        self.label_9.setText(_translate("MainWindow", "Array of frequences (Hz):"))
        self.label_13.setText(_translate("MainWindow", "Meters"))
        self.label_14.setText(_translate("MainWindow", "Meters"))
        self.label_15.setText(_translate("MainWindow", "Degrees"))
        self.label_16.setText(_translate("MainWindow", "Separated by a comma: , "))
        self.simulate1.setText(_translate("MainWindow", "Simulate"))
        self.save1.setText(_translate("MainWindow", "Save"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Room size: The size of the room to simulate in             \n"
"\n"
"Source Position: The position of the source in the room\n"
"\n"
"Temperature: Simulate the temperature in the room ( If not checked use a default tempurature)\n"
"\n"
"Humidity: Simulate the Humidity in the room ( If not checked use a default humidity)\n"
"\n"
"Air absorption: Simulate the Air absorption in the room ( If not checked there is no air absorption)\n"
"\n"
"Circulaire Array: Position the antennas in a circule of radius=\"Inter Mic Distance\"\n"
"\n"
"Linear Array: Position the antennas in a line distanced by \"Inter Mic Distance\"\n"
"\n"
"Center: Center of the Antennas Array\n"
"\n"
"Inter Antenna Distance: Distance between the antennas\n"
"\n"
"Angle: Antenna Angle\n"
"\n"
"Array of frequences: Simulate the beamforming for the specified frequences\n"
"\n"
"NB: you can use a big dimensions of the room to simulate as in a free space\n"
"\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Beamforming"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Original Source Location"))
        self.label_17.setText(_translate("MainWindow", "Azimuth:"))
        self.label_18.setText(_translate("MainWindow", "Distance:"))
        self.label_45.setText(_translate("MainWindow", "Degrees"))
        self.label_46.setText(_translate("MainWindow", "Meters"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Algorithms Parameters"))
        self.label_19.setText(_translate("MainWindow", "Signal to noise ratio (SNR):"))
        self.Sound.setText(_translate("MainWindow", "343.0"))
        self.Azimuth.setText(_translate("MainWindow", "61.0"))
        self.Distance.setText(_translate("MainWindow", "3"))
        self.SNR.setText(_translate("MainWindow", "0"))
        self.fs.setText(_translate("MainWindow", "16000"))
        self.minb.setText(_translate("MainWindow", "5"))
        self.maxb.setText(_translate("MainWindow", "60"))
        self.label_20.setText(_translate("MainWindow", "Speed of sound:"))
        self.label_21.setText(_translate("MainWindow", "Sampling Frequency: "))
        self.label_22.setText(_translate("MainWindow", "FFT size:"))
        self.ffts.setText(_translate("MainWindow", "256"))
        self.label_23.setText(_translate("MainWindow", "FFT bins for estimation:"))
        self.label_24.setText(_translate("MainWindow", "Min"))
        self.label_25.setText(_translate("MainWindow", "Max"))
        self.label_47.setText(_translate("MainWindow", "Hz"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Anechoic room Parameters"))
        self.checkBox_6.setText(_translate("MainWindow", "Tempurature"))
        self.checkBox_5.setText(_translate("MainWindow", "Air Absorption"))
        self.checkBox_4.setText(_translate("MainWindow", "Humidity"))
        self.label_35.setText(_translate("MainWindow", "Meters"))
        self.label_33.setText(_translate("MainWindow", "Y"))
        self.label_34.setText(_translate("MainWindow", "Room Size:                       X"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Antennas Parameters"))
        self.label_38.setText(_translate("MainWindow", "Number of Antenna: "))
        self.label_39.setText(_translate("MainWindow", "Inter Antenna Distance:"))
        self.label_40.setText(_translate("MainWindow", "Angle: "))
        self.label_43.setText(_translate("MainWindow", "Meters"))
        self.label_44.setText(_translate("MainWindow", "Degrees"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Available Algorithms"))
        self.music.setText(_translate("MainWindow", "MUSIC"))
        self.srp.setText(_translate("MainWindow", "SRP-PHAT"))
        self.cssm.setText(_translate("MainWindow", "CSSM"))
        self.waves.setText(_translate("MainWindow", "WAVES"))
        self.tops.setText(_translate("MainWindow", "TOPS"))
        self.label_36.setText(_translate("MainWindow", "\" Multiple emitter location and signal parameter estimation \""))
        self.label_37.setText(_translate("MainWindow", "\" A high-accuracy, low-latency technique for talker localization in reverberant environments \""))
        self.label_41.setText(_translate("MainWindow", "Coherent signal-subspace processing for the detection and estimation of angles of arrival"))
        self.label_42.setText(_translate("MainWindow", "Weighted average of signal subspaces for robust wideband direction finding"))
        self.label_48.setText(_translate("MainWindow", "New DOA estimator for wideband signals"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Logs"))
        self.label_52.setText(_translate("MainWindow", "Angle: "))
        self.label_54.setText(_translate("MainWindow", "Degrees"))
        self.label_50.setText(_translate("MainWindow", "Recovered azimuth:"))
        self.label_51.setText(_translate("MainWindow", "Error:"))
        self.label_53.setText(_translate("MainWindow", "MUSIC"))
        self.label_55.setText(_translate("MainWindow", "SRP-PHAT"))
        self.label_57.setText(_translate("MainWindow", "WAVES"))
        self.label_58.setText(_translate("MainWindow", "TOPS"))
        self.label_60.setText(_translate("MainWindow", "CSSM"))
        self.label_56.setText(_translate("MainWindow", "-"))
        self.label_61.setText(_translate("MainWindow", "-"))
        self.label_62.setText(_translate("MainWindow", "-"))
        self.label_63.setText(_translate("MainWindow", "-"))
        self.label_64.setText(_translate("MainWindow", "-"))
        self.label_66.setText(_translate("MainWindow", "-"))
        self.label_67.setText(_translate("MainWindow", "-"))
        self.label_68.setText(_translate("MainWindow", "-"))
        self.label_69.setText(_translate("MainWindow", "-"))
        self.label_70.setText(_translate("MainWindow", "-"))
        self.simulate2.setText(_translate("MainWindow", "Simulate"))
        self.save2.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Direction of arrival"))

        #Functionality of beamforming

        self.checkBox.stateChanged.connect(self.toggle1)
        self.checkBox_2.stateChanged.connect(self.toggle2)
        self.checkBox_3.stateChanged.connect(self.toggle3)
        self.simulate1.clicked.connect(self.simulateBeam)
        self.save1.clicked.connect(self.saveBeam)

        #Functionality of doa

        self.checkBox_4.stateChanged.connect(self.toggle5)
        self.checkBox_5.stateChanged.connect(self.toggle6)
        self.checkBox_6.stateChanged.connect(self.toggle4)
        self.simulate2.clicked.connect(self.simulateDoa)
        self.save2.clicked.connect(self.saveDao)

    def simulateBeam(self):

        if self.Temperature.isEnabled():
            t = float(self.Temperature.text())
        else:
            t = None

        if self.Humidity.isEnabled():
            h = float(self.Humidity.text())
        else:
            h = None

        if self.Air.isEnabled():
            a = float(self.Air.text())
        else:
            a = None

        if (
                self.X_value.text() == "" or self.Y_value.text() == "" or self.X_value_2.text() == "" or self.Y_value_2.text() == "" or self.number.text() == "" or self.c_x.text() == "" or self.c_y.text() == "" or self.inter.text() == "" or self.angle.text() == "" or self.freqs.text() == ""):
            self.error_dialog.exec_()
        else:
            self.main_beam(float(self.X_value.text()), float(self.Y_value.text()), float(self.X_value_2.text()),
                           float(self.Y_value_2.text()),
                           self.circular.isChecked(), int(self.number.text()), float(self.c_x.text()),
                           float(self.c_y.text()), float(self.inter.text()),
                           float(self.angle.text()), 8000, list(map(int, self.freqs.text().split(','))), t, h, a)

    def saveBeam(self):
        if self.Temperature.isEnabled():
            t = float(self.Temperature.text())
        else:
            t = None

        if self.Humidity.isEnabled():
            h = float(self.Humidity.text())
        else:
            h = None

        if self.Air.isEnabled():
            a = float(self.Air.text())
        else:
            a = None

        if (self.X_value.text() == "" or self.Y_value.text() == "" or self.X_value_2.text() == "" or
                self.Y_value_2.text() == "" or self.number.text() == "" or self.c_x.text() == "" or
                self.c_y.text() == "" or self.inter.text() == "" or self.angle.text() == "" or self.freqs.text() == ""):
            self.error_dialog.exec_()
        else:
            self.save_main_beam(float(self.X_value.text()), float(self.Y_value.text()), float(self.X_value_2.text()),
                                float(self.Y_value_2.text()),
                                self.circular.isChecked(), int(self.number.text()), float(self.c_x.text()),
                                float(self.c_y.text()), float(self.inter.text()),
                                float(self.angle.text()), 8000, list(map(int, self.freqs.text().split(','))), t, h, a)

    def main_beam(self, rs_x, rs_y, sp_x, sp_y, is_circular, mic_num, c_x, c_y, i_m_d, angle, room_frequency, freques,
                  room_temp=None, room_humidity=None, is_airAbsorption=None):
        # Create a rs_x by rs_y metres shoe box room
        room = pra.ShoeBox([rs_x, rs_y], fs=room_frequency, temperature=room_temp, humidity=room_humidity,
                           air_absorption=is_airAbsorption)

        # Add a source somewhere in the room
        room.add_source([sp_x, sp_y])

        # Create a linear array beamformer with 4 microphones
        # with angle 0 degrees and inter mic distance 10 cm
        if (is_circular):
            R = pra.circular_2D_array([c_x, c_y], mic_num, angle, i_m_d)
        else:
            R = pra.linear_2D_array([c_x, c_y], mic_num, angle, i_m_d)

        room.add_microphone_array(pra.Beamformer(R, room.fs))

        # Now compute the delay and sum weights for the beamformer
        room.mic_array.rake_delay_and_sum_weights(room.sources[0][:1])

        # plot the room and resulting beamformer
        room.plot(freq=freques, img_order=0, mic_marker_size=15)
        plt.title("Beamforming simulation")
        plt.legend(freques)
        plt.show()

    def save_main_beam(self, rs_x, rs_y, sp_x, sp_y, is_circular, mic_num, c_x, c_y, i_m_d, angle, room_frequency,
                       freques, room_temp=None, room_humidity=None, is_airAbsorption=None):
        # Create a rs_x by rs_y metres shoe box room
        room = pra.ShoeBox([rs_x, rs_y], fs=room_frequency, temperature=room_temp, humidity=room_humidity,
                           air_absorption=is_airAbsorption)

        # Add a source somewhere in the room
        room.add_source([sp_x, sp_y])

        # Create a linear array beamformer with 4 microphones
        # with angle 0 degrees and inter mic distance 10 cm
        if (is_circular):
            R = pra.circular_2D_array([c_x, c_y], mic_num, angle, i_m_d)
        else:
            R = pra.linear_2D_array([c_x, c_y], mic_num, angle, i_m_d)

        room.add_microphone_array(pra.Beamformer(R, room.fs))

        # Now compute the delay and sum weights for the beamformer
        room.mic_array.rake_delay_and_sum_weights(room.sources[0][:1])

        # plot the room and resulting beamformer
        room.plot(freq=freques, img_order=0)
        # plt.show()
        plt.savefig('./fig.png')

    def main_doa(self,az,di,S,c1,f,n,fbm,fbM,r_x,r_y,room_temp,room_humidity,is_airAbsorption,num, angle, raduis, algos,save):
        # We define a meaningful distance measure on the circle
        # Location of original source
        azimuth = az / 180.0 * np.pi
        distance = di
        SNR = S  # signal-to-noise ratio
        c = c1  # speed of sound
        fs = f  # sampling frequency
        nfft = n  # FFT size
        freq_bins = np.arange(fbm, fbM)  # FFT bins to use for estimation
        # compute the noise variance
        sigma2 = 10 ** (-SNR / 10) / (4.0 * np.pi * distance) ** 2
        # Create an anechoic room
        room_dim = np.r_[r_x, r_y]
        aroom = pra.ShoeBox(room_dim, fs=fs, max_order=0, sigma2_awgn=sigma2,temperature=room_temp,humidity=room_humidity,air_absorption=is_airAbsorption)
        # add the source
        source_location = room_dim / 2 + distance * np.r_[np.cos(azimuth), np.sin(azimuth)]
        source_signal = np.random.randn((nfft // 2 + 1) * nfft)
        aroom.add_source(source_location, signal=source_signal)
        # We use a circular array
        R = pra.circular_2D_array(room_dim / 2, num, angle,raduis)
        aroom.add_microphone_array(pra.MicrophoneArray(R, fs=aroom.fs))
        # run the simulation
        aroom.simulate()
        # Compute the STFT frames needed
        X = np.array(
            [
                pra.transform.stft.analysis(signal, nfft, nfft // 2).T
                for signal in aroom.mic_array.signals
            ]
        )
        for algo_name in algos:
            # Construct the new DOA object
            doa = pra.doa.algorithms[algo_name](R, fs, nfft, c=c)
            # this call here perform localization on the frames in X
            doa.locate_sources(X, freq_bins=freq_bins)
            doa.polar_plt_dirac()
            plt.title(algo_name)
            # doa.azimuth_recon contains the reconstructed location of the source
            if algo_name == "CSSM":
                self.label_62.setText('{:.2f}'.format(float(doa.azimuth_recon / np.pi * 180.0)))
                self.label_68.setText('{:.2f}'.format(float(circ_dist(azimuth, doa.azimuth_recon) / np.pi * 180.0)))
            if algo_name == "MUSIC":
                self.label_56.setText('{:.2f}'.format(float(doa.azimuth_recon / np.pi * 180.0)))
                self.label_66.setText('{:.2f}'.format(float(circ_dist(azimuth, doa.azimuth_recon) / np.pi * 180.0)))
            if algo_name == "SRP":
                self.label_61.setText('{:.2f}'.format(float(doa.azimuth_recon / np.pi * 180.0)))
                self.label_67.setText('{:.2f}'.format(float(circ_dist(azimuth, doa.azimuth_recon) / np.pi * 180.0)))
            if algo_name == "TOPS":
                self.label_64.setText('{:.2f}'.format(float(doa.azimuth_recon / np.pi * 180.0)))
                self.label_70.setText('{:.2f}'.format(float(circ_dist(azimuth, doa.azimuth_recon) / np.pi * 180.0)))
            if algo_name == "WAVES":
                self.label_63.setText('{:.2f}'.format(float(doa.azimuth_recon / np.pi * 180.0)))
                self.label_69.setText('{:.2f}'.format(float(circ_dist(azimuth, doa.azimuth_recon) / np.pi * 180.0)))

            if save:
                plt.savefig("./{}.png".format(algo_name))

        if not save:
            plt.show()
        

    def simulateDoa(self):
        if self.Temperature_2.isEnabled():
            t = float(self.Temperature_2.text())
        else:
            t = None

        if self.Humidity_2.isEnabled():
            h = float(self.Humidity_2.text())
        else:
            h = None

        if self.Air_2.isEnabled():
            a = float(self.Air_2.text())
        else:
            a = None

        alg= [self.music.isChecked(),self.srp.isChecked(),self.cssm.isChecked(),self.waves.isChecked(),self.tops.isChecked()]
        names = ["MUSIC","SRP","CSSM","WAVES","TOPS"]
        resul = []
        for name,algo in zip(names,alg):
            if algo == True:
                resul.append(name)
        if self.Azimuth.text()== "" or self.Distance.text()== "" or self.SNR.text()== "" or self.Sound.text()== "" or self.fs.text()== "" or self.ffts.text()== "" or self.minb.text()== "" or self.maxb.text()== "" or self.r_x.text() == "" or self.r_y.text() == "" or self.number_2.text()== "" or self.inter_2.text()== "" or self.angle_2.text()== "":
            self.error_dialog.exec_()
        else:
            self.main_doa(float(self.Azimuth.text()),float(self.Distance.text()),float(self.SNR.text()),float(self.Sound.text()),float(self.fs.text()),int(self.ffts.text()),int(self.minb.text()),int(self.maxb.text()),float(self.r_x.text()),float(self.r_y.text()),t,h,a,int(self.number_2.text()),float(self.angle_2.text()),float(self.inter_2.text()),resul,False)

    def saveDao(self):
        if self.Temperature_2.isEnabled():
            t = float(self.Temperature_2.text())
        else:
            t = None

        if self.Humidity_2.isEnabled():
            h = float(self.Humidity_2.text())
        else:
            h = None

        if self.Air_2.isEnabled():
            a = float(self.Air_2.text())
        else:
            a = None

        alg= [self.music.isChecked(),self.srp.isChecked(),self.cssm.isChecked(),self.waves.isChecked(),self.tops.isChecked()]
        names = ["MUSIC","SRP","CSSM","WAVES","TOPS"]
        resul = []
        for name,algo in zip(names,alg):
            if algo == True:
                resul.append(name)

        if self.Azimuth.text()== "" or self.Distance.text()== "" or self.SNR.text()== "" or self.Sound.text()== "" or self.fs.text()== "" or self.ffts.text()== "" or self.minb.text()== "" or self.maxb.text()== "" or self.r_x.text() == "" or self.r_y.text() == "" or self.number_2.text()== "" or self.inter_2.text()== "" or self.angle_2.text()== "":
            self.error_dialog.exec_()
        else:
            self.main_doa(float(self.Azimuth.text()),float(self.Distance.text()),float(self.SNR.text()),float(self.Sound.text()),float(self.fs.text()),int(self.ffts.text()),int(self.minb.text()),int(self.maxb.text()),float(self.r_x.text()),float(self.r_y.text()),t,h,a,int(self.number_2.text()),float(self.angle_2.text()),float(self.inter_2.text()),resul,True)


    def toggle1(self):
        self.Temperature.setEnabled(not self.Temperature.isEnabled())
    def toggle2(self):
        self.Humidity.setEnabled(not self.Humidity.isEnabled())
    def toggle3(self):
        self.Air.setEnabled(not self.Air.isEnabled())
    def toggle4(self):
        self.Temperature_2.setEnabled(not self.Temperature_2.isEnabled())
    def toggle5(self):
        self.Humidity_2.setEnabled(not self.Humidity_2.isEnabled())
    def toggle6(self):
        self.Air_2.setEnabled(not self.Air_2.isEnabled())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
