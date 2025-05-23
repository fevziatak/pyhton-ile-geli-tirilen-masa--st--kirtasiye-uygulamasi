# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarimlar/frmAyarlar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmAyarlar(object):
    def setupUi(self, frmAyarlar):
        frmAyarlar.setObjectName("frmAyarlar")
        frmAyarlar.resize(1936, 992)
        frmAyarlar.setStyleSheet("#frmAyarlar{\n"
"background-image: url(:/arkaplan/3607424.jpg);\n"
"}")
        self.scrollUrunler = QtWidgets.QScrollArea(frmAyarlar)
        self.scrollUrunler.setGeometry(QtCore.QRect(10, 100, 1521, 881))
        self.scrollUrunler.setStyleSheet("background-color: transparent; /* Tamamen şeffaf arka plan */\n"
"\n"
"\n"
"")
        self.scrollUrunler.setWidgetResizable(True)
        self.scrollUrunler.setObjectName("scrollUrunler")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -11, 1498, 5022))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.urunlerFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.urunlerFrame.setMinimumSize(QtCore.QSize(0, 5000))
        self.urunlerFrame.setStyleSheet("#urunlerFrame{\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.urunlerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.urunlerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.urunlerFrame.setObjectName("urunlerFrame")
        self.lbl1 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl1.setGeometry(QtCore.QRect(80, 10, 151, 131))
        self.lbl1.setStyleSheet("border-image: url(:/iconlar/silgi.jpg);\n"
"border-radius: 10px;")
        self.lbl1.setText("")
        self.lbl1.setObjectName("lbl1")
        self.lblFiat3 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat3.setGeometry(QtCore.QRect(540, 180, 101, 41))
        self.lblFiat3.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat3.setObjectName("lblFiat3")
        self.lblFiat2 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat2.setGeometry(QtCore.QRect(330, 180, 101, 41))
        self.lblFiat2.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat2.setObjectName("lblFiat2")
        self.lbl2 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl2.setGeometry(QtCore.QRect(290, 10, 151, 131))
        self.lbl2.setStyleSheet("border-image: url(:/iconlar/kalem.png);\n"
"border-radius: 10px;")
        self.lbl2.setText("")
        self.lbl2.setObjectName("lbl2")
        self.urunGuncelle1 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle1.setGeometry(QtCore.QRect(90, 220, 121, 41))
        self.urunGuncelle1.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle1.setText("")
        self.urunGuncelle1.setObjectName("urunGuncelle1")
        self.lbl4 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl4.setGeometry(QtCore.QRect(710, 10, 151, 131))
        self.lbl4.setStyleSheet("border-image: url(:/iconlar/kalemTiras.png);\n"
"border-radius: 10px;")
        self.lbl4.setText("")
        self.lbl4.setObjectName("lbl4")
        self.txt3 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt3.setGeometry(QtCore.QRect(520, 150, 111, 41))
        self.txt3.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt3.setObjectName("txt3")
        self.lblFiat1 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat1.setGeometry(QtCore.QRect(120, 180, 101, 41))
        self.lblFiat1.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat1.setObjectName("lblFiat1")
        self.lblFiat4 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat4.setGeometry(QtCore.QRect(760, 180, 101, 41))
        self.lblFiat4.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat4.setObjectName("lblFiat4")
        self.txt4 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt4.setGeometry(QtCore.QRect(690, 150, 211, 41))
        self.txt4.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt4.setObjectName("txt4")
        self.txt1 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt1.setGeometry(QtCore.QRect(110, 150, 91, 41))
        self.txt1.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt1.setObjectName("txt1")
        self.lbl3 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl3.setGeometry(QtCore.QRect(500, 10, 151, 131))
        self.lbl3.setStyleSheet("border-image: url(:/iconlar/defter.png);\n"
"border-radius: 10px;")
        self.lbl3.setText("")
        self.lbl3.setObjectName("lbl3")
        self.txt2 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt2.setGeometry(QtCore.QRect(310, 150, 111, 41))
        self.txt2.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt2.setObjectName("txt2")
        self.lblFiat4_6 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat4_6.setGeometry(QtCore.QRect(310, 540, 101, 41))
        self.lblFiat4_6.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat4_6.setText("")
        self.lblFiat4_6.setObjectName("lblFiat4_6")
        self.lbl8 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl8.setGeometry(QtCore.QRect(70, 370, 151, 131))
        self.lbl8.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl8.setText("")
        self.lbl8.setObjectName("lbl8")
        self.lblFiat4_7 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat4_7.setGeometry(QtCore.QRect(120, 540, 101, 41))
        self.lblFiat4_7.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat4_7.setText("")
        self.lblFiat4_7.setObjectName("lblFiat4_7")
        self.txt4_6 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt4_6.setGeometry(QtCore.QRect(240, 510, 211, 41))
        self.txt4_6.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt4_6.setText("")
        self.txt4_6.setObjectName("txt4_6")
        self.txt4_7 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt4_7.setGeometry(QtCore.QRect(50, 510, 211, 41))
        self.txt4_7.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt4_7.setText("")
        self.txt4_7.setObjectName("txt4_7")
        self.lbl4_7 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl4_7.setGeometry(QtCore.QRect(260, 370, 151, 131))
        self.lbl4_7.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl4_7.setText("")
        self.lbl4_7.setObjectName("lbl4_7")
        self.txt4_8 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt4_8.setGeometry(QtCore.QRect(660, 510, 211, 41))
        self.txt4_8.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt4_8.setText("")
        self.txt4_8.setObjectName("txt4_8")
        self.lbl4_8 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl4_8.setGeometry(QtCore.QRect(490, 370, 151, 131))
        self.lbl4_8.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl4_8.setText("")
        self.lbl4_8.setObjectName("lbl4_8")
        self.txt4_9 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt4_9.setGeometry(QtCore.QRect(470, 510, 211, 41))
        self.txt4_9.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt4_9.setText("")
        self.txt4_9.setObjectName("txt4_9")
        self.lbl4_9 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl4_9.setGeometry(QtCore.QRect(680, 370, 151, 131))
        self.lbl4_9.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl4_9.setText("")
        self.lbl4_9.setObjectName("lbl4_9")
        self.lblFiat4_8 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat4_8.setGeometry(QtCore.QRect(730, 540, 101, 41))
        self.lblFiat4_8.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat4_8.setText("")
        self.lblFiat4_8.setObjectName("lblFiat4_8")
        self.lblFiat4_9 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat4_9.setGeometry(QtCore.QRect(540, 540, 101, 41))
        self.lblFiat4_9.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat4_9.setText("")
        self.lblFiat4_9.setObjectName("lblFiat4_9")
        self.lbl5 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl5.setGeometry(QtCore.QRect(920, 10, 151, 131))
        self.lbl5.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl5.setText("")
        self.lbl5.setObjectName("lbl5")
        self.txt5 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt5.setGeometry(QtCore.QRect(900, 150, 211, 41))
        self.txt5.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt5.setText("")
        self.txt5.setObjectName("txt5")
        self.lblFiat5 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat5.setGeometry(QtCore.QRect(950, 180, 101, 41))
        self.lblFiat5.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat5.setText("")
        self.lblFiat5.setObjectName("lblFiat5")
        self.lblFiat6 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat6.setGeometry(QtCore.QRect(1150, 180, 101, 41))
        self.lblFiat6.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat6.setText("")
        self.lblFiat6.setObjectName("lblFiat6")
        self.lbl6 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl6.setGeometry(QtCore.QRect(1120, 10, 151, 131))
        self.lbl6.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl6.setText("")
        self.lbl6.setObjectName("lbl6")
        self.txt6 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt6.setGeometry(QtCore.QRect(1100, 150, 211, 41))
        self.txt6.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt6.setText("")
        self.txt6.setObjectName("txt6")
        self.lbl7 = QtWidgets.QLabel(self.urunlerFrame)
        self.lbl7.setGeometry(QtCore.QRect(1330, 10, 151, 131))
        self.lbl7.setStyleSheet("border-image: url(:/iconlar/);\n"
"border-radius: 10px;")
        self.lbl7.setText("")
        self.lbl7.setObjectName("lbl7")
        self.txt7 = QtWidgets.QLabel(self.urunlerFrame)
        self.txt7.setGeometry(QtCore.QRect(1310, 150, 211, 41))
        self.txt7.setStyleSheet("color:white;\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.txt7.setText("")
        self.txt7.setObjectName("txt7")
        self.lblFiat7 = QtWidgets.QLabel(self.urunlerFrame)
        self.lblFiat7.setGeometry(QtCore.QRect(1350, 170, 101, 41))
        self.lblFiat7.setStyleSheet("color:white;\n"
"font: 87 13pt \"Arial Black\";\n"
"")
        self.lblFiat7.setText("")
        self.lblFiat7.setObjectName("lblFiat7")
        self.urunSil1 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil1.setGeometry(QtCore.QRect(90, 270, 121, 41))
        self.urunSil1.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil1.setText("")
        self.urunSil1.setObjectName("urunSil1")
        self.urunGuncelle2 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle2.setGeometry(QtCore.QRect(310, 220, 121, 41))
        self.urunGuncelle2.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle2.setText("")
        self.urunGuncelle2.setObjectName("urunGuncelle2")
        self.urunSil2 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil2.setGeometry(QtCore.QRect(310, 270, 121, 41))
        self.urunSil2.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil2.setText("")
        self.urunSil2.setObjectName("urunSil2")
        self.urunSil3 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil3.setGeometry(QtCore.QRect(520, 270, 121, 41))
        self.urunSil3.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil3.setText("")
        self.urunSil3.setObjectName("urunSil3")
        self.urunGuncelle3 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle3.setGeometry(QtCore.QRect(520, 220, 121, 41))
        self.urunGuncelle3.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle3.setText("")
        self.urunGuncelle3.setObjectName("urunGuncelle3")
        self.urunGuncelle4 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle4.setGeometry(QtCore.QRect(730, 220, 121, 41))
        self.urunGuncelle4.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle4.setText("")
        self.urunGuncelle4.setObjectName("urunGuncelle4")
        self.urunSil4 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil4.setGeometry(QtCore.QRect(730, 270, 121, 41))
        self.urunSil4.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil4.setText("")
        self.urunSil4.setObjectName("urunSil4")
        self.urunGuncelle5 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle5.setGeometry(QtCore.QRect(940, 220, 121, 41))
        self.urunGuncelle5.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle5.setText("")
        self.urunGuncelle5.setObjectName("urunGuncelle5")
        self.urunSil5 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil5.setGeometry(QtCore.QRect(940, 270, 121, 41))
        self.urunSil5.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil5.setText("")
        self.urunSil5.setObjectName("urunSil5")
        self.urunGuncelle6 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle6.setGeometry(QtCore.QRect(1140, 220, 121, 41))
        self.urunGuncelle6.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle6.setText("")
        self.urunGuncelle6.setObjectName("urunGuncelle6")
        self.urunSil6 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil6.setGeometry(QtCore.QRect(1140, 270, 121, 41))
        self.urunSil6.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil6.setText("")
        self.urunSil6.setObjectName("urunSil6")
        self.urunGuncelle7 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle7.setGeometry(QtCore.QRect(1340, 220, 121, 41))
        self.urunGuncelle7.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle7.setText("")
        self.urunGuncelle7.setObjectName("urunGuncelle7")
        self.urunSil7 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil7.setGeometry(QtCore.QRect(1340, 270, 121, 41))
        self.urunSil7.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil7.setText("")
        self.urunSil7.setObjectName("urunSil7")
        self.urunGuncelle8 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle8.setGeometry(QtCore.QRect(110, 600, 121, 41))
        self.urunGuncelle8.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle8.setText("")
        self.urunGuncelle8.setObjectName("urunGuncelle8")
        self.urunSil8 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil8.setGeometry(QtCore.QRect(110, 650, 121, 41))
        self.urunSil8.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil8.setText("")
        self.urunSil8.setObjectName("urunSil8")
        self.urunGuncelle10 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle10.setGeometry(QtCore.QRect(520, 600, 121, 41))
        self.urunGuncelle10.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle10.setText("")
        self.urunGuncelle10.setObjectName("urunGuncelle10")
        self.urunSil9 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil9.setGeometry(QtCore.QRect(320, 650, 121, 41))
        self.urunSil9.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil9.setText("")
        self.urunSil9.setObjectName("urunSil9")
        self.urunGuncelle9 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle9.setGeometry(QtCore.QRect(320, 600, 121, 41))
        self.urunGuncelle9.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle9.setText("")
        self.urunGuncelle9.setObjectName("urunGuncelle9")
        self.urunSil10 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil10.setGeometry(QtCore.QRect(520, 650, 121, 41))
        self.urunSil10.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil10.setText("")
        self.urunSil10.setObjectName("urunSil10")
        self.urunGuncelle11 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunGuncelle11.setGeometry(QtCore.QRect(720, 600, 121, 41))
        self.urunGuncelle11.setStyleSheet("border-image: url(:/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-add.512.png);\n"
"border-image: url(:/butonlar/ugncl.png);\n"
"border-rodius:15px;")
        self.urunGuncelle11.setText("")
        self.urunGuncelle11.setObjectName("urunGuncelle11")
        self.urunSil11 = QtWidgets.QPushButton(self.urunlerFrame)
        self.urunSil11.setGeometry(QtCore.QRect(720, 650, 121, 41))
        self.urunSil11.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.urunSil11.setText("")
        self.urunSil11.setObjectName("urunSil11")
        self.verticalLayout.addWidget(self.urunlerFrame)
        self.scrollUrunler.setWidget(self.scrollAreaWidgetContents)
        self.label_5 = QtWidgets.QLabel(frmAyarlar)
        self.label_5.setGeometry(QtCore.QRect(1460, 20, 81, 21))
        self.label_5.setStyleSheet("color:white;\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(frmAyarlar)
        self.label_2.setGeometry(QtCore.QRect(1220, 5, 61, 51))
        self.label_2.setStyleSheet("border-image: url(:/iconlar/server.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(frmAyarlar)
        self.label_3.setGeometry(QtCore.QRect(1390, 5, 61, 51))
        self.label_3.setStyleSheet("border-image: url(:/iconlar/signal.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(frmAyarlar)
        self.label_4.setGeometry(QtCore.QRect(1290, 20, 71, 21))
        self.label_4.setStyleSheet("color:white;\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(frmAyarlar)
        self.label_9.setGeometry(QtCore.QRect(1630, 40, 81, 21))
        self.label_9.setStyleSheet("color:#20dad8;\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(frmAyarlar)
        self.label.setGeometry(QtCore.QRect(1560, 5, 61, 51))
        self.label.setStyleSheet("border-image: url(:/iconlar/user.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(frmAyarlar)
        self.label_6.setGeometry(QtCore.QRect(1630, 20, 81, 21))
        self.label_6.setStyleSheet("color:white;\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(frmAyarlar)
        self.label_8.setGeometry(QtCore.QRect(1460, 40, 81, 21))
        self.label_8.setStyleSheet("color:#20dad8;\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(frmAyarlar)
        self.label_7.setGeometry(QtCore.QRect(1290, 40, 71, 21))
        self.label_7.setStyleSheet("color:#20dad8;\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.listwdgSepet = QtWidgets.QListWidget(frmAyarlar)
        self.listwdgSepet.setGeometry(QtCore.QRect(1550, 100, 361, 421))
        self.listwdgSepet.setStyleSheet("#listwdgSepet{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    background-color: #002a41;\n"
"    border: 3px solid #002a41;  /* Çerçeve rengi ve kalınlığı */\n"
"    border-radius: 10px;        /* Köşe yuvarlama */\n"
"    padding: 10px;              /* İç boşluk */\n"
"    padding-top: 60px;\n"
"    padding-bottom: 200px\n"
"}\n"
"QListWidget::item {\n"
"    color: #ffffff; /* Yazı rengi */\n"
"    padding: 3px; /* İç boşluk */\n"
"    min-height: 10px; /* Öğenin minimum yüksekliği */\n"
"}")
        self.listwdgSepet.setObjectName("listwdgSepet")
        self.btnUrunGeriAl = QtWidgets.QPushButton(frmAyarlar)
        self.btnUrunGeriAl.setGeometry(QtCore.QRect(1570, 410, 141, 51))
        self.btnUrunGeriAl.setStyleSheet("border-image: url(:/butonlar/usıl.png);\n"
"border-rodius:15px;")
        self.btnUrunGeriAl.setText("")
        self.btnUrunGeriAl.setObjectName("btnUrunGeriAl")
        self.lineUrunEkleAd = QtWidgets.QLineEdit(frmAyarlar)
        self.lineUrunEkleAd.setGeometry(QtCore.QRect(1620, 170, 191, 41))
        self.lineUrunEkleAd.setStyleSheet("color:black;\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"text-align: center;          \n"
"vertical-align: middle;      \n"
"padding: 0;\n"
"")
        self.lineUrunEkleAd.setText("")
        self.lineUrunEkleAd.setObjectName("lineUrunEkleAd")
        self.lineUrunFiyat = QtWidgets.QLineEdit(frmAyarlar)
        self.lineUrunFiyat.setGeometry(QtCore.QRect(1620, 240, 191, 41))
        self.lineUrunFiyat.setStyleSheet("color:black;\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"text-align: center;          \n"
"vertical-align: middle;      \n"
"padding: 0;\n"
"")
        self.lineUrunFiyat.setText("")
        self.lineUrunFiyat.setObjectName("lineUrunFiyat")
        self.lineUrunGorselAdi = QtWidgets.QLineEdit(frmAyarlar)
        self.lineUrunGorselAdi.setGeometry(QtCore.QRect(1620, 320, 191, 41))
        self.lineUrunGorselAdi.setStyleSheet("color:black;\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"text-align: center;          \n"
"vertical-align: middle;      \n"
"padding: 0;\n"
"")
        self.lineUrunGorselAdi.setText("")
        self.lineUrunGorselAdi.setObjectName("lineUrunGorselAdi")
        self.label_12 = QtWidgets.QLabel(frmAyarlar)
        self.label_12.setGeometry(QtCore.QRect(1610, 110, 271, 31))
        self.label_12.setStyleSheet("color:white;\n"
"font: 87 18pt \"Arial Black\";\n"
"")
        self.label_12.setObjectName("label_12")
        self.btnUrunKaydet = QtWidgets.QPushButton(frmAyarlar)
        self.btnUrunKaydet.setGeometry(QtCore.QRect(1740, 410, 141, 51))
        self.btnUrunKaydet.setAutoFillBackground(False)
        self.btnUrunKaydet.setStyleSheet("border-image: url(:/butonlar/URNKYDT.png);\n"
"border-rodius:15px;")
        self.btnUrunKaydet.setText("")
        self.btnUrunKaydet.setObjectName("btnUrunKaydet")
        self.btnUrunGeriAl_2 = QtWidgets.QPushButton(frmAyarlar)
        self.btnUrunGeriAl_2.setGeometry(QtCore.QRect(1730, 10, 141, 51))
        self.btnUrunGeriAl_2.setStyleSheet("\n"
"border-image: url(:/butonlar/8.jpg);\n"
"border-rodius:15px;")
        self.btnUrunGeriAl_2.setText("")
        self.btnUrunGeriAl_2.setObjectName("btnUrunGeriAl_2")

        self.retranslateUi(frmAyarlar)
        QtCore.QMetaObject.connectSlotsByName(frmAyarlar)

    def retranslateUi(self, frmAyarlar):
        _translate = QtCore.QCoreApplication.translate
        frmAyarlar.setWindowTitle(_translate("frmAyarlar", "Form"))
        self.lblFiat3.setText(_translate("frmAyarlar", "65 TL"))
        self.lblFiat2.setText(_translate("frmAyarlar", "15 TL"))
        self.txt3.setText(_translate("frmAyarlar", "defter"))
        self.lblFiat1.setText(_translate("frmAyarlar", "20 TL"))
        self.lblFiat4.setText(_translate("frmAyarlar", "10 TL"))
        self.txt4.setText(_translate("frmAyarlar", "kalemtraş"))
        self.txt1.setText(_translate("frmAyarlar", "silgi"))
        self.txt2.setText(_translate("frmAyarlar", "kalem"))
        self.label_5.setText(_translate("frmAyarlar", "Internet"))
        self.label_4.setText(_translate("frmAyarlar", "Server"))
        self.label_9.setText(_translate("frmAyarlar", "Bağlı"))
        self.label_6.setText(_translate("frmAyarlar", "User"))
        self.label_8.setText(_translate("frmAyarlar", "Bağlı"))
        self.label_7.setText(_translate("frmAyarlar", "Bağlı"))
        self.lineUrunEkleAd.setPlaceholderText(_translate("frmAyarlar", "Ürün Adı"))
        self.lineUrunFiyat.setPlaceholderText(_translate("frmAyarlar", "Ürün Fiyatı"))
        self.lineUrunGorselAdi.setPlaceholderText(_translate("frmAyarlar", "Görsel adı"))
        self.label_12.setText(_translate("frmAyarlar", "Ürün Ekle"))
import arkaplanlar_rc
import butonlar_rc
import iconlar_rc
