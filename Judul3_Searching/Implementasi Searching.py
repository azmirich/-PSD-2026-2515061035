# Sequential Search
def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter

def main():
    data = ["Buku Cerita", "Buku Matematika Diskrit", "Buku Catatan", "Buku Struktur Data", "Buku Aljabar Matrix", "Buku Novel"]
    n = len(data)
    print(f"Buku di dalam tas: {data}")
    while True:
        try:
            target = input("Masukkan nama buku yang ingin dicari: ")
            break
        except ValueError:
            print("Input tidak valid")
    counter = sequential_search(data, n, target)
    if counter > 0:
        print(f"Buku '{target}' ditemukan sebanyak {counter} kali.")
    else:
        print(f"Buku '{target}' tidak ditemukan.")

if __name__ == "__main__":
    main()