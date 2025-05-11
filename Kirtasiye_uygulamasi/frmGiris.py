from PyQt5 import QtWidgets
import sys
import pymysql
from donusumler.frmGirisEkraniUİ import Ui_frmGirisEkrani
from frmAnasayfa import frmAnasayfa  # Ana sayfa import edildi

# Global bağlantı nesnesi
baglanti = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="Izvef*1453mysql",
    db="kirtasiye_database",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)

print("Bağlantı başarılı!")

class frmGiris(QtWidgets.QMainWindow):
    def __init__(self):
        super(frmGiris, self).__init__()
        self.ui = Ui_frmGirisEkrani()
        self.ui.setupUi(self)
        self.cursor = baglanti.cursor()  # Global bağlantıdan cursor alıyoruz

        # Çıkış butonunu bul ve olay ekle
        self.ui.btnCikis.clicked.connect(self.close_application)
        self.ui.btnGiris.clicked.connect(self.check_login)  # Giriş butonuna olay ekle

    def check_login(self):
        # Kullanıcı adı ve şifreyi al
        kullanici_adi = self.ui.lbllKullaniciAdi.text()  # lblKullaniciAdi ile doğru adı kullandığınızdan emin olun
        sifre = self.ui.lblSifre.text()  # lblSifre ile doğru adı kullandığınızdan emin olun

        try:
            # Veritabanında sorgu yap
            self.cursor.execute("SELECT * FROM personeller WHERE personel_isim = %s", (kullanici_adi,))
            kullanici = self.cursor.fetchone()

            if kullanici:
                # Kullanıcı adı bulundu, şifreyi kontrol et
                if kullanici["personel_sifre"] == sifre:
                    self.show_message("Başarılı", "Kullanıcı adı ve şifre doğru")
                    self.open_anasayfa()  # Ana sayfaya geçiş
                else:
                    self.show_message("Hata", "Şifre hatalı")
            else:
                self.show_message("Hata", "Kullanıcı adı hatalı")
        except Exception as e:
            self.show_message("Sorgu Hatası", f"Sorgu sırasında hata oluştu: {e}")

    def open_anasayfa(self):
        # Giriş başarılı olduğunda ana sayfayı aç
        self.anasayfa = frmAnasayfa()  # Ana sayfa sınıfını oluştur
        self.anasayfa.show()  # Ana sayfayı göster
        self.close()  # Giriş ekranını kapat

    def close_application(self):
        # Uygulama kapanırken veritabanı bağlantısını kapat
        try:
            if baglanti and baglanti.open:
                baglanti.close()
                self.show_message("Başarı", "Veri tabanı bağlantısı kapatıldı.")
        except Exception as e:
            self.show_message("Bağlantı Hatası", f"Bağlantı kapatma hatası: {e}")
        self.close()  # Pencereyi kapat

    def closeEvent(self, event):
        # Pencere kapanırken veritabanı bağlantısını kapat
        self.close_application()
        event.accept()

    def show_message(self, title, message):
        """Mesaj kutusu ile kulanıcıya bilgi verir"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)  # İkonu belirleyin (Bilgi ikonu)
        msg.setWindowTitle(title)  # Başlık
        msg.setText(message)  # Mesaj
        msg.exec_()  # Mesaj kutusunu göster

def baslat():
    uygulama = QtWidgets.QApplication(sys.argv)
    pencere = frmGiris()
    pencere.show()
    sys.exit(uygulama.exec_())

if __name__ == "__main__":
    baslat()
