import subprocess
import os

# .qrc dosyasının yolu ve çıktı dosyasının yolu
qrc_file = r"C:\Users\HP\OneDrive\Masaüstü\qt_demo_apk\sistemResimleri\iconlar\iconlar.qrc"  # Türkçe karakteri değiştirdik
output_file = r"C:\Users\HP\OneDrive\Masaüstü\qt_demo_apk\iconlar_rc.py"  # Çıktı dosyasının yolu

# pyrcc5 komutunu çalıştırmak
command = ['pyrcc5', qrc_file, '-o', output_file]

# Komutu çalıştır
try:
    subprocess.run(command, check=True)
    print("Dönüştürme başarılı!")
except subprocess.CalledProcessError as e:
    print(f"Bir hata oluştu: {e}")
