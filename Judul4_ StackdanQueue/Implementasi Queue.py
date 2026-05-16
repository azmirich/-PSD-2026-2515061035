class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1
        self.size = 0

    def is_empty(self):
        return self.front_idx == -1
    
    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Queue penuh")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"Nomor antrean {x} berhasil ditambahkan ke sistem antrian ATM. Estimasi waktu tunggu adalah {self.size * 3} menit.")
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong")
            return
        print(f"Nomor antrean {self.q[self.front_idx]} silakan menuju ke mesin/loket ATM")
        self.size -= 1
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Queue kosong")
            return
        print(f"No antrean terdepan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Queue kosong")
            return
        print("Isi antrian (depan ke belakang): ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()


def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== ANTRIAN LOKET ATM ===")
        print("1. Enqueue (Ambil Nomor Antrean)")
        print("2. Dequeue (Panggil Nomor Berikutnya)")
        print("3. Peek (Lihat Nomor Antrean Terdepan)")
        print("4. Tampilkan Isi Antrian")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = int(input("Masukkan nomor antrean: "))
                queue.enqueue(val)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()