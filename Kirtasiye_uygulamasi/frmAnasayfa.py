from donusumler.frmAnasayfaUİ import Ui_frmAnaSayfa
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import pymysql
import os
from PyQt5.QtGui import QPixmap
from functools import partial
from frmAyarlar import frmAyarlar
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QListWidgetItem
from PyQt5.QtGui import QIcon


baglanti = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="Izvef*1453mysql",
    db="kirtasiye_database",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)



class frmAnasayfa(QtWidgets.QMainWindow):
    def __init__(self):
        super(frmAnasayfa, self).__init__()
        self.ui = Ui_frmAnaSayfa()
        self.ui.setupUi(self)
        self.cursor = baglanti.cursor()

        # Butonları bağlantıya ekleyelim
        self.btn_clicekd()
        self.ui.btnSepetGuncelle.clicked.connect(self.sepet_guncelle)
        self.ui.btnIndirimKaldir.clicked.connect(self.indirim_kaldir)  # İndirim kaldırma butonu

        self.toplamFiyat = 0.0  # Başlangıçta toplam fiyat
        self.sepet = {}  # Sepetteki ürünleri ve adetlerini tutacak bir sözlük
        self.indirim_yapildi = False  # İlk başta indirim yapılmamış
        self.indirim_orani = 0  # İndirim oranını sakla
        self.toplam_fiyat_onceki = 0.0  # İndirim öncesi toplam fiyat

        self.ürün_ekle()
        # Buton tıklama olayını bağlama
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.ui.btnOdeme.clicked.connect(self.odeme_al)
        self.goster_sepet()

    def goster_sepet(self):
        # UI üzerindeki sepeti güncelle
        self.ui.listwdgSepet.clear()  # ListWidget'ı temizle
        for urun_ad, urun in self.sepet.items():
            self.ui.listwdgSepet.addItem(f"{urun_ad}: {urun['adet']} x {urun['fiyat']} TL")

    def odeme_al(self):
        # Fiş bilgilerini hazırlıyoruz
        toplam_fiyat = 0
        fiş_metni = ""

        for urun_ad, urun in self.sepet.items():
            urun_toplam = urun['adet'] * urun['fiyat']
            fiş_metni += f"{urun['adet']}x{urun_ad} {urun_toplam} TL\n"
            toplam_fiyat += urun_toplam

        # KDV hesaplama (örneğin %18)
        kdv = toplam_fiyat * 0.10

        # Fişin tamamlanmış metni
        fiş_metni += f"\nKDV: {kdv:.2f} TL"
        fiş_metni += f"\nToplam Fiyat: {toplam_fiyat:.2f} TL"

        # Message Box gösterme
        msg = QMessageBox(self)
        msg.setWindowTitle("Ödeme Alındı")
        msg.setText(fiş_metni)  # Fiş metnini ekliyoruz
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

        self.toplamFiyat = 0.0

        # İndirimleri sıfırlıyoruz
        self.indirim_yapildi = False
        self.indirim_orani = 0
        self.toplam_fiyat_onceki = 0.0

        # Sepeti boşaltıyoruz
        self.sepet.clear()
        self.guncelle_toplam_fiyat()  # Toplam fiyatı güncelle
        self.guncelle_kdv()

        # UI üzerindeki sepeti de temizliyoruz
        self.goster_sepet()  # Arayüzü güncelle

    def btn_clicekd(self):
        for i in range(1, 12):  # 1'den 11'e kadar
            btn_name = f"btnSepetekle{i}"  # Butonun adı: btnSepetekle1, btnSepetekle2, ...
            button = getattr(self.ui, btn_name, None)  # Butonu dinamik olarak al

            if button:
                button.clicked.connect(partial(self.sepet_ekle_ürün,
                                               i))  # Butona tıklandığında, sepet_ekle_ürün fonksiyonunu ürün_id ile bağla

    def btn_gizle(self):
        for sayac in range(1, 12):  # 1'den 11'e kadar döngü
            # Etiket adını oluştur
            btn_sepet_ekle_field_name = f"btnSepetekle{sayac}"

            # Etiketi al
            btn_sepet_ekle_field = getattr(self.ui, btn_sepet_ekle_field_name, None)

            # Etiket var mı kontrol et
            if btn_sepet_ekle_field:
                btn_sepet_ekle_field.setHidden(True)  # Butonu gizle
            else:
                print(f"{btn_sepet_ekle_field_name} bulunamadı")

    def btn_gizle(self):
        for sayac in range(1, 12):  # 1'den 11'e kadar döngü
            # Etiket adını oluştur
            btn_sepet_ekle_field_name = f"btnSepetekle{sayac}"

            # Etiketi al
            btn_sepet_ekle_field = getattr(self.ui, btn_sepet_ekle_field_name, None)

            # Etiket var mı kontrol et
            if btn_sepet_ekle_field:
                btn_sepet_ekle_field.setHidden(True)  # Butonu gizle
            else:
                print(f"{btn_sepet_ekle_field_name} bulunamadı")


    def btn_gizleme(self, ürün_id):
        btn_sepet_ekle_field_name = f"btnSepetekle{ürün_id}"

        # Etiketi al
        btn_sepet_ekle_field = getattr(self.ui, btn_sepet_ekle_field_name, None)

        # Etiket var mı kontrol et
        if btn_sepet_ekle_field:
            btn_sepet_ekle_field.setHidden(False)  # Butonu göster
        else:
            print(f"{btn_sepet_ekle_field_name} bulunamadı")

    def get_fiyat_from_label(self, label):
        """
        Verilen label'in içeriğinden fiyat bilgisini alır.
        """
        return label.text().strip()  # Etiketin içindeki yazıyı olduğu gibi alır

    def sepet_ekle_ürün(self, ürün_id):
        try:
            self.cursor.execute("SELECT ürün_adi FROM ürünler WHERE ürün_id = %s", (ürün_id,))
            urun_adi_ = self.cursor.fetchone()
            self.cursor.execute("SELECT ürün_fiyat FROM ürünler WHERE ürün_id = %s", (ürün_id,))
            urun_fiyat_ = self.cursor.fetchone()

            if urun_adi_ is None or urun_fiyat_ is None:
                raise ValueError("Ürün verileri alınamadı.")

            urun_adi = urun_adi_['ürün_adi']
            fiyat = urun_fiyat_['ürün_fiyat']
            self.sepet_ekle(urun_adi, fiyat)
        except Exception as e:
            print(f"Hata: {e}")
            QMessageBox.warning(self, "Hata", f"Ürün eklenemedi: {e}")

    def ürün_txt_ekle(self,ürün_id):
        self.cursor.execute("SELECT ürün_adi FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()  # Sadece ilk satırı alıyoruz

        if urun:
            urun_ad = urun['ürün_adi']  # Ürün adını al
            print(f'Ürün Adı: {urun_ad}')  # Ürün adını ekrana yazdır

            # ID'ye göre doğru txt etiketine yazdırma
            txt_field_name = f"txt{ürün_id}"  # txt1, txt2, ... şeklinde etiket adı oluştur
            txt_field = getattr(self.ui, txt_field_name, None)  # Etiketi al

            if txt_field:
                txt_field.setText(urun_ad)  # Ürün adını txt etiketi üzerine yazdır
            else:
                print(f"txt{ürün_id} bulunamadı")  # Eğer etiket bulunamazsa hata mesajı
        else:
            print(f"{ürün_id} id'li ürün bulunamadı")  # Eğer ürün bulunamazsa mesaj

    def ürün_fiat_ekle(self,ürün_id):
        self.cursor.execute("SELECT ürün_fiyat FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()  # Sadece ilk satırı alıyoruz

        if urun:
            urun_fiyat = urun['ürün_fiyat']  # Ürün adını al
            print(f'Ürün Fiyatı: {urun_fiyat}')  # Ürün adını ekrana yazdır

            # ID'ye göre doğru txt etiketine yazdırma
            txt_field_name = f"lblFiat{ürün_id}"  # txt1, txt2, ... şeklinde etiket adı oluştur
            txt_field = getattr(self.ui, txt_field_name, None)  # Etiketi al

            if txt_field:
                txt_field.setText(urun_fiyat)  # Ürün adını txt etiketi üzerine yazdır
            else:
                print(f"txt{ürün_id} bulunamadı")  # Eğer etiket bulunamazsa hata mesajı
        else:
            print(f"{ürün_id} id'li ürün bulunamadı")  # Eğer ürün bulunamazsa mesaj

    def ürün_görsel_ekle(self, ürün_id):
        # Veritabanından ürünün resim yolunu almak için sorgu
        self.cursor.execute("SELECT image_yolu FROM ürünler WHERE ürün_id = %s", (ürün_id,))
        urun = self.cursor.fetchone()  # Sadece ilk satırı alıyoruz

        if urun:
            image_yolu = urun['image_yolu']  # image_yolu değerini al
            image_path = os.path.join(os.path.dirname(__file__), "sistemResimleri", "iconlar",
                                      image_yolu)  # Yolu tam olarak oluştur

            if os.path.exists(image_path):  # Eğer resim dosyası mevcutsa
                pixmap = QPixmap(image_path)  # Resmi yükle
                txt_field_name = f"lbl{ürün_id}"  # lbl1, lbl2,... şeklinde etiket ismini oluştur
                lbl_field = getattr(self.ui, txt_field_name, None)  # Dinamik olarak lbl etiketini al

                if lbl_field:
                    lbl_field.setPixmap(pixmap)  # Resmi QLabel'a yerleştir
                    lbl_field.setScaledContents(True)  # Resmi QLabel'a uyacak şekilde ölçeklendir
                else:
                    print(f"lbl{ürün_id} bulunamadı")  # Eğer etiket bulunamazsa hata mesajı
            else:
                print(f"Resim dosyası bulunamadı: {image_path}")  # Eğer resim dosyası bulunamazsa hata mesajı
        else:
            print(f"{ürün_id} id'li ürün için resim yolu bulunamadı.")  # Eğer resim yolu bulunamazsa mesaj

    def ürün_ekle(self):
        self.btn_gizle()
        self.cursor.execute("SELECT ürün_id FROM ürünler")  # ürün_id sütunundaki verileri al
        ids = self.cursor.fetchall()  # Veritabanından gelen tüm satırları al

        # ids listesi üzerinde döngü kurma
        for row in ids:
            ürün_id = row['ürün_id']  # 'ürün_id' anahtarını kullanarak değeri al
            print(f'Ürün ID: {ürün_id}')

            # Her bir ürün_id için ürün adını almak için sorgu
            self.ürün_txt_ekle(ürün_id)
            self.ürün_fiat_ekle(ürün_id)
            self.ürün_görsel_ekle(ürün_id)
            self.btn_gizleme(ürün_id)

    def sepet_ekle(self, urun_adi, fiyat):
        try:
            fiyat = fiyat.replace("TL", "").strip()  # 'TL' kısmını çıkar ve boşlukları temizle
            fiyat = float(fiyat)  # Fiyatı float'a dönüştür
        except ValueError:
            print(f"Hata: Geçersiz fiyat formatı: {fiyat}")
            QMessageBox.warning(self, "Hata", "Geçersiz fiyat formatı.")
            return

        # Sepetteki ürünün adedini kontrol et ve güncelle
        if urun_adi in self.sepet:
            self.sepet[urun_adi]['adet'] += 1  # Aynı üründen eklenirse adedi artır
            self.sepet[urun_adi]['toplam_fiyat'] = self.sepet[urun_adi]['adet'] * self.sepet[urun_adi][
                'fiyat']  # Toplam fiyatı güncelle
        else:
            self.sepet[urun_adi] = {'fiyat': fiyat, 'adet': 1,
                                    'toplam_fiyat': fiyat}  # Yeni ürün ekle ve toplam fiyatını belirle

        self.toplamFiyat += fiyat  # Toplam fiyata ürünü ekle
        self.guncelle_sepet()  # Sepeti güncelle
        self.guncelle_toplam_fiyat()  # Toplam fiyatı güncelle
        self.guncelle_kdv()  # KDV'yi güncelle

    def guncelle_sepet(self):
        # Sepeti listeye yazdır
        self.ui.listwdgSepet.clear()  # ListView temizle

        for urun_adi, urun_bilgisi in self.sepet.items():
            # Yeni bir widget oluştur
            item_widget = QWidget()
            layout = QHBoxLayout(item_widget)

            # Ürün bilgisi etiketi
            urun_text = f"{urun_bilgisi['adet']}x {urun_adi} {urun_bilgisi['toplam_fiyat']:.2f} TL"
            urun_label = QLabel(urun_text)
            urun_label.setStyleSheet("font: 87 8pt 'Arial Black';color: #ffffff; padding: 3px; min-height: 10px;")
            layout.addWidget(urun_label)

            # Buton oluştur ve bağla
            sil_btn = QPushButton()
            sil_btn.setFixedSize(30, 30)  # Butonun boyutunu belirleyin

            # Resmi butona ekle
            sil_btn.setIcon(QIcon(':/iconlar/Custom-Icon-Design-Flatastic-4-Shopping-cart-remove.512.png'))

            # Resmin butona göre oranlı bir şekilde ayarlanmasını sağla
            sil_btn.setIconSize(sil_btn.size())  # Resmi butona göre boyutlandır
            sil_btn.setStyleSheet("background-color: transparent; border: none;")

            sil_btn.clicked.connect(lambda _, urun=urun_adi: self.sepetten_sil(urun))  # Silme fonksiyonuna bağla
            layout.addWidget(sil_btn)

            # ListWidget öğesi olarak ekle
            list_item = QListWidgetItem(self.ui.listwdgSepet)
            list_item.setSizeHint(item_widget.sizeHint())
            self.ui.listwdgSepet.addItem(list_item)
            self.ui.listwdgSepet.setItemWidget(list_item, item_widget)

    def sepetten_sil(self, urun_adi):
        if urun_adi in self.sepet:
            urun_bilgisi = self.sepet[urun_adi]
            self.toplamFiyat -= urun_bilgisi['toplam_fiyat']  # Toplam fiyattan düş
            del self.sepet[urun_adi]  # Sepetten ürünü kaldır

            self.guncelle_sepet()  # Sepeti güncelle
            self.guncelle_toplam_fiyat()  # Toplam fiyatı güncelle
            self.guncelle_kdv()  # KDV'yi güncelle

    def guncelle_toplam_fiyat(self):
        # Toplam fiyatı sadece sayısal olarak lblToplamFiat üzerine yazdır
        self.ui.lblToplamFiat.setText(f"{self.toplamFiyat:.2f}")  # Sadece fiyat kısmını yazdır

    def guncelle_kdv(self):
        # KDV'yi hesapla ve lblKdv'ye yazdır
        kdv = self.toplamFiyat * 0.10  # %10 KDV hesapla
        self.ui.lblKdv.setText(f"{kdv:.2f}")  # KDV'yi etiket üzerine yazdır

    def sepet_guncelle(self):
        # İndirim işlemi
        if not self.indirim_yapildi:
            try:
                indirim = float(self.ui.lineIndirim.text())  # İndirim oranını al
                if 1 <= indirim <= 100:  # 1 ile 100 arasında olmalı
                    # İndirim oranını kaydet
                    self.indirim_orani = indirim
                    self.toplam_fiyat_onceki = self.toplamFiyat  # Eski toplam fiyatı sakla

                    # Toplam fiyattan indirim yap
                    self.toplamFiyat -= (self.toplamFiyat * (indirim / 100))
                    self.guncelle_toplam_fiyat()  # Toplam fiyatı güncelle
                    self.indirim_yapildi = True  # İndirim yapıldığını işaretle
                else:
                    # Geçersiz indirim oranı
                    QMessageBox.warning(self, "Hata", "Lütfen 1 ile 100 arasında bir değer giriniz.")
            except ValueError:
                # Hatalı giriş
                QMessageBox.warning(self, "Hata", "Lütfen geçerli bir indirim oranı giriniz.")
        else:
            QMessageBox.warning(self, "Hata", "İndirim zaten yapıldı. Tekrar indirim yapamazsınız.")

    def indirim_kaldir(self):
        if self.indirim_yapildi:
            self.toplamFiyat = self.toplam_fiyat_onceki  # Eski fiyatı geri yükle
            self.indirim_yapildi = False  # İndirim yapıldığını işaretle
            self.guncelle_toplam_fiyat()  # Toplam fiyatı güncelle
            self.ui.lineIndirim.clear()   # İndirim alanını temizle
            QMessageBox.information(self, "Bilgi", "İndirim kaldırıldı.")
        else:
            QMessageBox.warning(self, "Hata", "Hiçbir indirim yapılmadı.")

    def pushButton_2_clicked(self):
        # frmAyarlar sayfasını aç
        self.frm_Ayarlar = frmAyarlar()  # frmAyarlar sınıfını çağır
        self.frm_Ayarlar.show()  # Sayfayı göster

        # frmAnasayfa sayfasını kapat
        self.close()


def baslat():
    uygulama = QtWidgets.QApplication(sys.argv)
    pencere = frmAnasayfa()
    pencere.show()
    sys.exit(uygulama.exec_())


if __name__ == '__main__':
    baslat()
