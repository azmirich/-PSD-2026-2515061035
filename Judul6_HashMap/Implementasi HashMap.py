#SISTEMMANAJEMENSTOKLUXURYCARSHOWROOM
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None


    def display(self):
        print("\nIsi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()
    
    while True:
        print("\n=== SISTEM MANAJEMEN STOK LUXURY CAR SHOWROOM ===")
        print("1. Tambah Mobil Ready")
        print("2. Tampilkan Daftar Mobil")
        print("3. Cari Status Mobil")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            try:
                key = int(input("Masukkan Kode Mobil: "))
                value = input("Masukkan Merek dan Tipe Mobil: ")
                hashmap.insert(key, value)
                print(f"Berhasil! {value} masuk ke daftar mobil ready.")
            except ValueError:
                print("Error: Kode Mobil harus berupa angka!")
                
        elif pilihan == '2':
            hashmap.display()
            
        elif pilihan == '3':
            try:
                key = int(input("Masukkan Kode Mobil yang ingin dicari: "))
                hasil = hashmap.search(key)
                if hasil is not None:
                    print(f"\n=> Ditemukan! Mobil ready: {hasil.value}")
                else:
                    print("\n=> Mobil Sudah Sold Out/Sudah di Booking.")
            except ValueError:
                print("Error: Kode Mobil harus berupa angka!")
                
        elif pilihan == '4':
            print("Keluar dari sistem. Terima kasih Telah Mengunjungi LUXURY CAR SHOWROOM!")
            break
            
        else:
            print("Pilihan tidak valid, silakan coba lagi!")

if __name__ == "__main__":
    main()