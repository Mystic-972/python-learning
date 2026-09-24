bilangan = []

jumlah = 0

for i in range(1, 6):
    nilai = int(input(f"Masukkan nilai ke-{i} : "))
    bilangan.append(nilai)
    jumlah += nilai

maks = bilangan[0]
minimum = bilangan[0]

for i in range(1, 5):
    if bilangan[i] > maks:
        maks = bilangan[i]
    if bilangan[i] < minimum:
        minimum = bilangan[i]

rata_rata = jumlah / 5

print()
print("Berikut adalah data yang anda input")
for nilai in bilangan:
    print(nilai, end=" ")

print()
print(f"Jumlah data     : 5")
print(f"Rata rata       : {rata_rata:.2f}")
print(f"Nilai tertinggi : {maks}")
print(f"Nilai terendah  : {minimum}")

input()
