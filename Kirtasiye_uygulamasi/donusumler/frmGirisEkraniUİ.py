# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarimlar/frmGirisEkrani.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmGirisEkrani(object):
    def setupUi(self, frmGirisEkrani):
        frmGirisEkrani.setObjectName("frmGirisEkrani")
        frmGirisEkrani.resize(465, 537)
        frmGirisEkrani.setStyleSheet("#frmGirisEkrani{\n"
"     background-color:#004b66;\n"
"}")
        self.btnGiris = QtWidgets.QPushButton(frmGirisEkrani)
        self.btnGiris.setGeometry(QtCore.QRect(220, 360, 151, 41))
        self.btnGiris.setStyleSheet("#btnGiris {\n"
"    background-color:#ff8521; /* Kırmızımsı bir ton */\n"
"    color:#004b66;           /* Beyaz yazı rengi */\n"
"    font-family: \'Arial\';\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    border: 2px solid #ff8521;\n"
"}\n"
"\n"
"#btnGiris:hover {\n"
"    background-color:#f4c997; /* Hover durumu için daha koyu ton */\n"
"    color: #004b66;\n"
"}\n"
"\n"
"#btnGiris:pressed {\n"
"    background-color: #ff8521; /* Basıldığında daha koyu kırmızı */\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"")
        self.btnGiris.setObjectName("btnGiris")
        self.lbllKullaniciAdi = QtWidgets.QLineEdit(frmGirisEkrani)
        self.lbllKullaniciAdi.setGeometry(QtCore.QRect(50, 210, 341, 51))
        self.lbllKullaniciAdi.setStyleSheet("    background-color:#f4c997; /* Kırmızımsı bir ton */\n"
"    color:#004b66;           /* Beyaz yazı rengi */\n"
"    font-family: \'Arial\';\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 25px;\n"
"    padding: 10px;\n"
"    border: 2px solid #f4c997;")
        self.lbllKullaniciAdi.setText("")
        self.lbllKullaniciAdi.setObjectName("lbllKullaniciAdi")
        self.lblSifre = QtWidgets.QLineEdit(frmGirisEkrani)
        self.lblSifre.setGeometry(QtCore.QRect(50, 290, 341, 51))
        self.lblSifre.setStyleSheet("    background-color:#f4c997; /* Kırmızımsı bir ton */\n"
"    color:#004b66;           /* Beyaz yazı rengi */\n"
"    font-family: \'Arial\';\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 25px;\n"
"    padding: 10px;\n"
"    border: 2px solid #f4c997;")
        self.lblSifre.setObjectName("lblSifre")
        self.btnCikis = QtWidgets.QPushButton(frmGirisEkrani)
        self.btnCikis.setGeometry(QtCore.QRect(70, 360, 131, 41))
        self.btnCikis.setStyleSheet("#btnCikis {\n"
"    background-color:#ff8521; /* Kırmızımsı bir ton */\n"
"    color:#004b66;           /* Beyaz yazı rengi */\n"
"    font-family: \'Arial\';\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 20px;\n"
"    padding: 10px;\n"
"    border: 2px solid #ff8521;\n"
"}\n"
"\n"
"#btnCikis:hover {\n"
"    background-color:#f4c997; /* Hover durumu için daha koyu ton */\n"
"    color: #004b66;\n"
"}\n"
"\n"
"#btnCikis:pressed {\n"
"    background-color: #ff8521; /* Basıldığında daha koyu kırmızı */\n"
"    border: 2px solid #FFFFFF;\n"
"}\n"
"")
        self.btnCikis.setObjectName("btnCikis")
        self.label = QtWidgets.QLabel(frmGirisEkrani)
        self.label.setGeometry(QtCore.QRect(20, 20, 491, 81))
        self.label.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: #FFD700; /* Sarı renk */\n"
"    font-size: 48px; /* Yazı boyutu */\n"
"    font-weight: bold; /* Kalın yazı */\n"
"    text-transform: uppercase; /* Büyük harf yapma */\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmGirisEkrani)
        self.label_2.setGeometry(QtCore.QRect(250, 110, 291, 41))
        self.label_2.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"color: white; /* Sarı renk */\n"
"    font-size: 48px; /* Yazı boyutu */\n"
"    font-weight: bold; /* Kalın yazı */\n"
"    text-transform: uppercase; /* Büyük harf yapma */\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(frmGirisEkrani)
        QtCore.QMetaObject.connectSlotsByName(frmGirisEkrani)

    def retranslateUi(self, frmGirisEkrani):
        _translate = QtCore.QCoreApplication.translate
        frmGirisEkrani.setWindowTitle(_translate("frmGirisEkrani", "Kullanıcı Girişi"))
        self.btnGiris.setText(_translate("frmGirisEkrani", "Giriş Yap "))
        self.lbllKullaniciAdi.setPlaceholderText(_translate("frmGirisEkrani", "Kullanıcı adı"))
        self.lblSifre.setPlaceholderText(_translate("frmGirisEkrani", "Şifre"))
        self.btnCikis.setText(_translate("frmGirisEkrani", "Çıkış Yap"))
        self.label.setText(_translate("frmGirisEkrani", "Kullanıcı"))
        self.label_2.setText(_translate("frmGirisEkrani", "Girişi"))
