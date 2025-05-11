import subprocess

tasarimlar = [
    "tasarimlar/frmAnasayfa.ui"
]

for tasarim in tasarimlar:
    py_dosya = f"donusumler/{tasarim.split('/')[-1].replace('.ui', 'Uİ')}.py"

    komut = ["pyuic5",tasarim,"-o",py_dosya]

    try:

        subprocess.run(komut,check=True)
        print(f"{tasarim} dönüştürüldü")

    except subprocess.CalledProcessError:
        print(f"{tasarim} hata...")
