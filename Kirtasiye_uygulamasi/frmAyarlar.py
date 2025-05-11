from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import pymysql
import os
from donusumler.frmAyarlarUİ import Ui_frmAyarlar
from functools import partial
# Veritabanı bağlantısı
baglanti = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="Izvef*1453mysql",
    db="kirtasiye_database",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


class frmAyarlar(QtWidgets.QMainWindow):
    def __init__(self):
        super(frmAyarlar, self).__init__()
        self.ui = Ui_frmAyarlar()
        self.ui.setupUi(self)
        self.cursor = baglanti.cursor()

        # Butonları dinamik olarak bağlama
        self.btn_Güncelle_clicekd()
        self.urun_ekle()
        self.ui.btnUrunKaydet.clicked.connect(self.urun_kaydet)
        self.ui.btnUrunGeriAl.clicked.connect(self.urun_geri_al)

        self.urun_id = None  # Başlangıçta ürün ID'si yok (yeni ürün ekleme)
        self.urun_sil_butonlari()
        self.ui.btnUrunGeriAl_2.clicked.connect(self.AnasayfaDon_clicked)

    def AnasayfaDon_clicked(self):
        from frmAnasayfa import frmAnasayfa
        # frmAyarlar sayfasını aç
        self.frm_Anasayfa = frmAnasayfa()  # frmAyarlar sınıfını çağır
        self.frm_Anasayfa.show()  # Sayfayı göster

        # frmAnasayfa sayfasını kapat
        self.close()

    def urun_sil_butonlari(self):
        for i in range(1, 12):  # Ürün ID'lerini 1'den 11'e kadar kontrol et
            btn_name = f"urunSil{i}"  # Buton adı: urunSil1, urunSil2
            button = getattr(self.ui, btn_name, None)  # Butonu dinamik olarak al

            if button:
                button.clicked.connect(partial(self.urun_sil, i))  # Her butona tıklanıldığında urun_sil fonksiyonunu çağır


    def urun_sil(self, ürün_id):
        # Ürün ID'sine göre veritabanında silme işlemi yapalım
        try:
            self.cursor.execute("DELETE FROM ürünler WHERE ürün_id = %s", (ürün_id,))
            baglanti.commit()
            self.cursor.execute("SELECT MAX(ürün_id) AS max_id FROM ürünler")
            max_id = self.cursor.fetchone()['max_id']

            # AUTO_INCREMENT değerini en yüksek id'yi geçecek şekilde ayarla
            if max_id is not None:
                self.cursor.execute("ALTER TABLE ürünler AUTO_INCREMENT = %s", (max_id + 1,))
                baglanti.commit()

            print(f"{ürün_id} ID'li ürün silindi ve AUTO_INCREMENT değeri güncellendi.")

            QtWidgets.QMessageBox.information(self, "Başarılı", f"{ürün_id} ID'li ürün başarıyla silindi.")

            # Silinen ürüne ait tüm bilgileri temizle
            self.ürün_txt_ekle(ürün_id)
            self.ürün_fiat_ekle(ürün_id)
            self.ürün_görsel_ekle(ürün_id)

            # Silinen ürünün butonlarını gizle
            self.btn_gizleme(ürün_id)

        except Exception as e:
            print("Hata:", e)
            QtWidgets.QMessageBox.critical(self, "Hata", f"{ürün_id} ID'li ürün silinirken bir hata oluştu.")

    def urun_kaydet(self):
        urun_ad = self.ui.lineUrunEkleAd.text()
        urun_fiyat = self.ui.lineUrunFiyat.text()
        urun_gorsel = self.ui.lineUrunGorselAdi.text()

        if not urun_ad or not urun_fiyat or not urun_gorsel:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        if self.urun_id:
            try:
                self.cursor.execute("""
                    UPDATE ürünler 
                    SET ürün_adi = %s, ürün_fiyat = %s, image_yolu = %s 
                    WHERE ürün_id = %s
                """, (urun_ad, urun_fiyat, urun_gorsel, self.urun_id))
                baglanti.commit()

                QtWidgets.QMessageBox.information(self, "Başarılı", "Ürün başarıyla güncellendi.")
                self.ui.lineUrunEkleAd.clear()
                self.ui.lineUrunFiyat.clear()
                self.ui.lineUrunGorselAdi.clear()
                self.urun_id = None
                self.ui.label_12.setText("Ürün Güncelleme Başarılı!")
            except Exception as e:
                print("Hata:", e)
                QtWidgets.QMessageBox.critical(self, "Hata", "Ürün güncellenirken bir hata oluştu.")
        else:
            try:
                self.cursor.execute("INSERT INTO ürünler (ürün_adi, ürün_fiyat, image_yolu) VALUES (%s, %s, %s)",
                                    (urun_ad, urun_fiyat, urun_gorsel))
                baglanti.commit()

                QtWidgets.QMessageBox.information(self, "Başarılı", "Ürün başarıyla eklendi.")
                self.ui.lineUrunEkleAd.clear()
                self.ui.lineUrunFiyat.clear()
                self.ui.lineUrunGorselAdi.clear()
                self.ui.label_12.setText("Ürün Ekleme Başarılı!")
            except Exception as e:
                print("Hata:", e)
                QtWidgets.QMessageBox.critical(self, "Hata", "Ürün eklenirken bir hata oluştu.")

    def urun_geri_al(self):
        # Line edit'leri temizle
        self.ui.lineUrunEkleAd.clear()
        self.ui.lineUrunFiyat.clear()
        self.ui.lineUrunGorselAdi.clear()

        # label_12'yi eski haline döndür
        self.ui.label_12.setText("Ürün Ekle")  # Burada eski metni istediğiniz gibi ayarlayabilirsiniz

        # Eğer bir ürün güncelleniyorsa, urun_id'yi sıfırlama
        self.urun_id = None
    def btn_Güncelle_clicekd(self):
        for i in range(1, 12):  # 1'den 11'e kadar
            btn_name = f"urunGuncelle{i}"  # Butonun adı: urunGuncelle1, urunGuncelle2, ...
            button = getattr(self.ui, btn_name, None)  # Butonu dinamik olarak al

            if button:
                button.clicked.connect(partial(self.btn_guncelle, i))  # Butona tıklandığında btn_guncelle'yi bağla
            else:
                print(f"{btn_name} bulunamadı")  # Buton yoksa hata mesajı ver

    def btn_guncelle(self, ürün_id):
        # Eğer bir ürün güncelleniyorsa, urun_id'yi set et
        self.urun_id = ürün_id
        # Butona tıklanınca line edit'lere mevcut ürün bilgilerini yazdır
        self.cursor.execute("SELECT ürün_adi, ürün_fiyat, image_yolu FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()
        if urun:
            self.ui.lineUrunEkleAd.setText(urun['ürün_adi'])
            self.ui.lineUrunFiyat.setText(str(urun['ürün_fiyat']))
            self.ui.lineUrunGorselAdi.setText(urun['image_yolu'])
            # label_12'yi güncelle
            self.ui.label_12.setText(f"{urun['ürün_adi']} Düzenleniyor...")

    def btn_gizle(self):
        for sayac in range(1, 12):  # 1'den 11'e kadar döngü
            urunGuncelle_field_name = f"urunGuncelle{sayac}"
            urunSil_field_name = f"urunSil{sayac}"

            urunGuncelle_field = getattr(self.ui, urunGuncelle_field_name, None)
            urunSil_field = getattr(self.ui, urunSil_field_name, None)

            if urunGuncelle_field:
                urunGuncelle_field.setHidden(True)

            if urunSil_field:
                urunSil_field.setHidden(True)

    def btn_gizleme(self, ürün_id):
        urunGuncelle_field_name = f"urunGuncelle{ürün_id}"
        urunSil_field_name = f"urunSil{ürün_id}"

        urunGuncelle_field = getattr(self.ui, urunGuncelle_field_name, None)
        urunSil_field = getattr(self.ui, urunSil_field_name, None)

        if urunGuncelle_field:
            urunGuncelle_field.setHidden(False)

        if urunSil_field:
            urunSil_field.setHidden(False)

    def ürün_txt_ekle(self, ürün_id):
        self.cursor.execute("SELECT ürün_adi FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()  # Sadece ilk satırı alıyoruz

        if urun:
            urun_ad = urun['ürün_adi']  # Ürün adını al
            print(f'Ürün Adı: {urun_ad}')

            txt_field_name = f"txt{ürün_id}"
            txt_field = getattr(self.ui, txt_field_name, None)

            if txt_field:
                txt_field.setText(urun_ad)  # Ürün adını txt etiketi üzerine yazdır
            else:
                print(f"txt{ürün_id} bulunamadı")
        else:
            print(f"{ürün_id} id'li ürün bulunamadı")

    def ürün_fiat_ekle(self, ürün_id):
        self.cursor.execute("SELECT ürün_fiyat FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()

        if urun:
            urun_fiyat = urun['ürün_fiyat']
            print(f'Ürün Fiyatı: {urun_fiyat}')

            txt_field_name = f"lblFiat{ürün_id}"
            txt_field = getattr(self.ui, txt_field_name, None)

            if txt_field:
                txt_field.setText(str(urun_fiyat))
            else:
                print(f"lblFiat{ürün_id} bulunamadı")
        else:
            print(f"{ürün_id} id'li ürün bulunamadı")

    def ürün_görsel_ekle(self, ürün_id):
        self.cursor.execute("SELECT image_yolu FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()

        if urun:
            image_yolu = urun['image_yolu']
            image_path = os.path.join(os.path.dirname(__file__), "sistemResimleri", "iconlar", image_yolu)

            if os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                txt_field_name = f"lbl{ürün_id}"
                lbl_field = getattr(self.ui, txt_field_name, None)

                if lbl_field:
                    lbl_field.setPixmap(pixmap)
                    lbl_field.setScaledContents(True)
                else:
                    print(f"lbl{ürün_id} bulunamadı")
            else:
                print(f"Resim dosyası bulunamadı: {image_path}")
        else:
            print(f"{ürün_id} id'li ürün için resim yolu bulunamadı.")

    def urun_ekle(self):
        self.btn_gizle()
        self.cursor.execute("SELECT ürün_id FROM ürünler")
        ids = self.cursor.fetchall()

        for row in ids:
            ürün_id = row['ürün_id']
            print(f'Ürün ID: {ürün_id}')

            self.ürün_txt_ekle(ürün_id)
            self.ürün_fiat_ekle(ürün_id)
            self.ürün_görsel_ekle(ürün_id)
            self.btn_gizleme(ürün_id)


def baslat():
    uygulama = QtWidgets.QApplication(sys.argv)
    pencere = frmAyarlar()  # Nesne oluşturuluyor
    pencere.show()  # Pencereyi gösteriyoruz
    sys.exit(uygulama.exec_())  # Uygulama döngüsünü başlatıyoruz


if __name__ == '__main__':
    baslat()
