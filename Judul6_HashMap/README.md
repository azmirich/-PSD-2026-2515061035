Sistem Manajemen Stok Luxury Car Showroom
Implementasi Hash Map  Separate Chaining

Program ini mensimulasikan sistem manajemen stok mobil pada sebuah Luxury Car Showroom menggunakan struktur data Hash Map dengan metode Separate Chaining.
Pengguna dapat:
Menambah data mobil ready stok
Menampilkan seluruh isi hash table
Mencari status mobil berdasarkan kode

SOURCE CODE :

INPUT
<img width="281" height="107" alt="image" src="https://github.com/user-attachments/assets/5e8eb0db-6b13-44a3-b468-c3e52b9d2a12" />

class Node:Mendefinisikan blueprint/cetakan untuk setiap node (simpul) dalam linked list
def__init__(self, key, value):Konstruktor — dipanggil otomatis saat node baru dibuat. Menerima key (kode mobil) dan value (merek & tipe)
self.key = keyMenyimpan kode mobil (misal: 101) ke dalam node ini
self.value = valueMenyimpan nama mobil  ke dalam node ini
self.next = NonePointer ke node berikutnya dalam linked list. Awalnya None karena belum terhubung ke mana-mana


<img width="327" height="88" alt="image" src="https://github.com/user-attachments/assets/759a8e28-b447-4e1f-be5a-e2bee320cd2f" />


class HashMapSeparateChaining:Mendefinisikan class utama yang berisi seluruh logika hash map
def __init__(self, size=10):Konstruktor dengan parameter default size=10 — tabel akan punya 10 slot jika tidak diubah
self.SIZE = sizeMenyimpan ukuran tabel (jumlah slot yang tersedia)
self.table = [None] * self.SIZEMembuat list berisi 10 elemen None — mewakili 10 slot kosong di hash table


<img width="413" height="45" alt="image" src="https://github.com/user-attachments/assets/c9c0a1cb-4f29-4e45-bc5f-71f8132b9144" />


def hash_function(self, key):Fungsi yang mengubah key menjadi nomor index tabel
key % self.SIZEOperasi modulo — mengambil sisa bagi key dengan ukuran tabel. Hasilnya selalu antara 0 sampai SIZE-1


<img width="316" height="220" alt="image" src="https://github.com/user-attachments/assets/a0842ee9-2c7c-47f0-864a-080e3d5e96e8" />


index = self.hash_function(key) Hitung index tujuan menggunakan hash function
current = self.table[index] Ambil node pertama di slot tersebut (bisa None jika kosong)
while current is not None: Telusuri linked list selama masih ada node
if current.key == key: Cek apakah kode mobil sudah ada sebelumnya
current.value = value Jika sudah ada → update valuenya (bukan tambah duplikat)
returnKeluar dari fungsi setelah updatecurrent = current.next Geser pointer ke node berikutnya
new_node = Node(key, value) Buat node baru jika kode belum ada
new_node.next = self.table [index]Hubungkan node baru ke node yang sudah ada di slot tersebut
self.table[index] = new_node Taruh node baru di paling depan linked list (insert at head)


<img width="314" height="160" alt="image" src="https://github.com/user-attachments/assets/710af581-8561-477a-b9a4-250eeb943cdc" />


index = self.hash_function(key)Cari tahu di slot mana kunci ini seharusnya berada
current = self.table[index]Mulai dari node pertama di slot tersebut
while current is not None:Telusuri semua node dalam linked list di slot itu
if current.key == key:Jika kode cocok...return current...kembalikan node tersebut (berhasil ditemukan)
current = current.nextKalau belum cocok, geser ke node berikutnya
return NoneJika habis ditelusuri tapi tidak ketemu → kembalikan none


<img width="527" height="188" alt="image" src="https://github.com/user-attachments/assets/3251c752-4842-47f1-871c-4697819234e4" />


for i in range(self.SIZE):Iterasi dari index 0 sampai 9 (semua slot tabel)
print(f"{i}: ", end="")Cetak nomor index, end="" agar tidak pindah baris dulu
current = self.table[i]Ambil node pertama di slot ke-i
while current is not None:Telusuri seluruh linked list di slot ini
print(f"({current.key},{current.value}) -> ", end="")Cetak pasangan key-value dan tanda panah ->
current = current.nextGeser ke node berikutnya
print("NULL")Cetak NULL di akhir linked list — menandakan rantai berakhir


<img width="536" height="216" alt="image" src="https://github.com/user-attachments/assets/31dba6bc-e307-4a8f-9da6-b84fc37dca97" />


hashmap = HashMapSeparateChaining()Buat objek hash map baru dengan 10 slot default
while True:Loop tak terbatas — program terus berjalan sampai user memilih keluar
print(...)Tampilkan menu pilihan ke layar
pilihan = input(...)Tunggu dan baca pilihan dari pengguna


<img width="505" height="163" alt="image" src="https://github.com/user-attachments/assets/e33b94b8-6aaa-4365-9a14-f15233e428b0" />


if pilihan == '1':Jika user memilih menu 1
try:Mulai blok percobaan — antisipasi kemungkinan error
key = int(input(...))Minta input kode mobil dan konversi ke integer
value = input(...)Minta input merek dan tipe mobil
hashmap.insert(key, value)Panggil fungsi insert untuk menyimpan data
except ValueError:Tangkap error jika user memasukkan bukan angka


<img width="658" height="392" alt="image" src="https://github.com/user-attachments/assets/971bfd9a-517f-41b7-a8aa-c0754071ccf9" />


elif pilihan == '2':Menu 2 → panggil display() untuk tampilkan semua data
elif pilihan == '3':Menu 3 → cari data berdasarkan kode mobil
hasil = hashmap.search(key)Simpan hasil pencarian ke variabel hasil
if hasil is not None:Jika ditemukan → tampilkan nama mobil
else:Jika tidak ditemukan → mobil sold out/dibooking
break Menu 4 → hentikan loop, program selesai
else: print("Pilihan tidak valid...")Jika input bukan 1-4 → tampilkan pesan error


<img width="225" height="61" alt="image" src="https://github.com/user-attachments/assets/dc46a7af-07ea-479c-8007-a0ee3b850752" />


Menjalankan fungsi utama



OUTPUT


<img width="377" height="490" alt="image" src="https://github.com/user-attachments/assets/89af7287-58b4-40f5-a985-a413e8c8cbeb" />


<img width="517" height="320" alt="image" src="https://github.com/user-attachments/assets/3d2861ad-5545-40c9-a29f-b7c49a1dd9f7" />


Video Penjelasan : 
