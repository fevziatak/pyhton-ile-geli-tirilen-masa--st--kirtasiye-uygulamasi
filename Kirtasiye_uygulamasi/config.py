import pymysql

try:
    baglanti = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='Izvef*1453mysql',
        db='kirtasiye_database',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Bağlantı başarılı!")


    with baglanti.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")  # Bağlanılan veritabanını kontrol et
        result = cursor.fetchone()
        print("Bağlanılan veritabanı:", result['DATABASE()'])

except pymysql.MySQLError as e:
    print("Hata:", e)

finally:
    # Bağlantıyı kapat
    if 'baglanti' in locals() and baglanti.open:
        baglanti.close()
        print("Bağlantı kapatıldı.")
