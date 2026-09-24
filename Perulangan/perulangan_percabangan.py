jumlah_siswa = int(input("Masukkan jumlah siswa : "))

for i in range(1, jumlah_siswa + 1):
    print(f"\nData siswa ke-{i}")

    nama = input("Nama siswa : ")
    nilai = int(input("Nilai : "))

    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    elif nilai >= 60:
        grade = "D"
    else:
        grade = "E"

    if nilai >= 70:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print(f"Nama   : {nama}")
    print(f"Nilai  : {nilai}")
    print(f"Grade  : {grade}")
    print(f"Status : {status}")
