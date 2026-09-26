import os

def luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f"Luas Segitiga adalah: {luas:.2f}")

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas Persegi Panjang adalah: {luas:.2f}")

def luas_lingkaran(jari_jari):
    phi = 3.14
    luas = phi * jari_jari * jari_jari
    print(f"Luas Lingkaran adalah: {luas:.2f}")

lanjut = "Y"

while lanjut.upper() != "T":
    os.system("cls" if os.name == "nt" else "clear")

    print("========================================")
    print("  Program Menghitung Luas Bangun Datar")
    print("========================================")
    print("1. Luas Segitiga")
    print("2. Luas Persegi Panjang")
    print("3. Luas Lingkaran")
    print("========================================")

    pilihan = int(input("Pilih menu (1-3): "))
    print()

    if pilihan == 1:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga(alas, tinggi)

    elif pilihan == 2:
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas_persegi_panjang(panjang, lebar)

    elif pilihan == 3:
        jari_jari = float(input("Masukkan jari jari lingkaran: "))
        luas_lingkaran(jari_jari)

    else:
        print("Pilihan tidak valid! Silakan masukkan angka 1, 2, atau 3.")

    print()
    lanjut = input("Apakah Anda ingin menghitung lagi? (Y/T): ")

print()
print("Terima kasih telah menggunakan program ini!")
