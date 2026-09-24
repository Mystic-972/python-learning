import os

os.system("cls" if os.name == "nt" else "clear")

A = [[0 for _ in range(10)] for _ in range(10)]
B = [[0 for _ in range(10)] for _ in range(10)]
C = [[0 for _ in range(10)] for _ in range(10)]

bA = int(input("Banyak baris matriks ke 1 : "))
kA = int(input("Banyak kolom matriks ke 1 : "))
bB = int(input("Banyak baris matriks ke 2 : "))
kB = int(input("Banyak kolom matriks ke 2 : "))

if kA != bB:
    print("ERROR: Kolom matriks 1 harus sama dengan baris matriks 2 !")
    input()
    exit()

print("Matriks pertama :")
for i in range(bA):
    for j in range(kA):
        A[i][j] = int(input(f"  A[{i + 1},{j + 1}] = "))

print("Matriks kedua :")
for i in range(bB):
    for j in range(kB):
        B[i][j] = int(input(f"  B[{i + 1},{j + 1}] = "))

print("Proses perkalian")
for i in range(bA):
    for j in range(kB):
        for k in range(kA):
            if k < kA - 1:
                print(f"{A[i][k]} . {B[k][j]} + ", end="")
            else:
                print(f"{A[i][k]} . {B[k][j]}", end="")
        print("   ", end="")
    print()

for i in range(bA):
    for j in range(kB):
        C[i][j] = 0
        for k in range(kA):
            C[i][j] += A[i][k] * B[k][j]

print("Perkalian Matriks :")
for i in range(bA):
    for j in range(kB):
        print(f"{C[i][j]:8}", end="")
    print()

input()
