def menu():
    print("\nList Nilai Mahasiswa")
    print("1. Tampilkan address list nilai mahasiswa")
    print("2. Tampilkan address dari semua index list")
    print("3. Masukkan nilai mahasiswa")
    print("4. Keluar")


def main():
    nilai = [0] * 5
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print(f"Address list nilai mahasiswa: {id(nilai)}")
        elif choice == 2:
            for i in range(5):
                print(f"Address nilai[{i}]: {id(nilai[i])}")
        elif choice == 3:
            print("Masukkan 5 nilai mahasiswa:")
            for i in range(5):
                while True:
                    try:
                        nilai[i] = int(input(f"nilai[{i}] = "))
                        break
                    except ValueError:
                        print("Input tidak valid, masukkan angka!")
            print(f"List nilai mahasiswa: {nilai}")
        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()