def main():
    print("Mencetak bintang")

    for baris in range(1, 4):
        for _ in range(baris):
            print("*", end="")
        print()


if __name__ == "__main__":
    main()
