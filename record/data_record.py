def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def main():
    mahasiswa = []

    jumlah = int(input("Berapa Jumlah Mahasiswa : "))
    print()

    for i in range(1, jumlah + 1):
        print(f"Mahasiswa ke-{i}")

        nim = input("NIM   : ")
        nama = input("Nama  : ")
        tugas = float(input("Tugas : "))
        uts = float(input("UTS   : "))
        uas = float(input("UAS   : "))

        data = {
            "nim": nim,
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas
        }

        mahasiswa.append(data)
        print()

    print("-" * 75)
    print(f"{'NO':<4}{'NIM':<12}{'NAMA':<15}{'TUGAS':>8}{'UTS':>8}{'UAS':>8}{'NA':>8}{'GRADE':>8}")
    print("-" * 75)

    for i, mhs in enumerate(mahasiswa, start=1):
        nilai_akhir = (mhs["tugas"] + mhs["uts"] + mhs["uas"]) / 3
        grade = tentukan_grade(nilai_akhir)

        print(
            f"{i:<4}"
            f"{mhs['nim']:<12}"
            f"{mhs['nama']:<15}"
            f"{mhs['tugas']:>8.2f}"
            f"{mhs['uts']:>8.2f}"
            f"{mhs['uas']:>8.2f}"
            f"{nilai_akhir:>8.2f}"
            f"{grade:>8}"
        )

    print("-" * 75)


if __name__ == "__main__":
    main()
