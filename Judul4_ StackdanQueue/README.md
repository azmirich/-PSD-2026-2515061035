Program Antrian Loket ATM—Queue Array

Simulasi sistem antrian loket ATM menggunakan struktur data Queue berbasis Array Sirkular (Circular Array Queue) yang diimplementasikan dalam bahasa Python.
Saya menggunakan Array karena sangat sesuai menggunakan sistem FIFO (First In First Out) sesuai dengan antrian di dunia nyata

Program ini mensimulasikan sistem antrian nasabah di loket ATM. Setiap nasabah mendapat nomor antrean dan akan dipanggil secara FIFO (First In, First Out)
siapa yang datang lebih dulu, dilayani lebih dulu. Program juga memberikan estimasi waktu tunggu berdasarkan jumlah orang yang sedang mengantre.

Source Code :

INPUT

<img width="139" height="21" alt="image" src="https://github.com/user-attachments/assets/13a11a9f-c6c3-414f-bca5-5b8b44419050" />
Class utama yang mengimplementasikan struktur data Queue menggunakan array sirkular.

<img width="272" height="118" alt="image" src="https://github.com/user-attachments/assets/081123b2-7310-4977-9085-87fbffa8d000" />
Kapasitas maksimum queue
Array berisi MAXN slot, semua diisi None sebagai "kosong"
Self Size penghitung jumlah elemen aktif di dalam queue
Nilai -1 dipakai sebagai penanda "queue kosong" karena indeks array valid selalu ≥ 0. Saat pertama kali ada elemen masuk, front_idx dan rear_idx akan di-set ke 0.

<img width="252" height="45" alt="image" src="https://github.com/user-attachments/assets/a8b381d8-06de-4948-8813-366fb614d929" />
is_empty untuk mengecek Apakah Queue Kosong
Mengembalikan True jika front_idx masih bernilai -1, yang artinya belum ada elemen yang pernah masuk, atau semua elemen sudah dikeluarkan.

<img width="486" height="49" alt="image" src="https://github.com/user-attachments/assets/a0330e2f-2ff2-45be-b979-61b77b5decd4" />
Untuk mengecek apakah Queue penuh
Queue dinyatakan penuh jika posisi tepat setelah rear_idx (dihitung secara melingkar menggunakan modulo %) kembali bertemu dengan front_idx.

<img width="1003" height="235" alt="image" src="https://github.com/user-attachments/assets/1e7cd509-07a7-4ec0-86ef-02cd98bb439d" />
enqueue = Menambah Elemen
self.front_idx = 0 Elemen pertama: reset front ke indeks 0
self.rear_idx = 0 Sekaligus set rear ke indeks 0
self.rear_idx = (self.rear_idx + 1) % self.MAXN Geser rear ke slot berikutnya (melingkar)
self.q[self.rear_idx] = x Simpan nilai x di posisi rear yang baru
self.size += 1 menambah penghitung elemen
self.size * 3 dihitung SEBELUM size += 1? Karena nasabah baru berada di posisi size (0-based), jadi orang di depannya ada sebanyak size orang, masing-masing butuh 3 menit.

<img width="680" height="213" alt="image" src="https://github.com/user-attachments/assets/48f9befc-0690-432b-9eb1-067fd6de63d1" />
dequeue = Mengeluarkan Elemen (Nasabah Dipanggil)
print("Queue kosong") Tidak bisa memanggil jika tidak ada antrean
if self.front_idx == self.rear_idx: Elemen terakhir baru saja dikeluarkan → reset queue ke kondisi kosong
Pengecekan front_idx == rear_idx sebelum menggeser penting agar tidak terjadi kondisi "queue terlihat kosong tapi front/rear masih menunjuk ke posisi lama".


<img width="490" height="107" alt="image" src="https://github.com/user-attachments/assets/d16876e7-cf5c-4d8b-a595-94a6a24e1f32" />
peek = Melihat Elemen/Antian Terdepan
peek tidak mengubah front_idx maupun size. Hanya membaca nilai di posisi front_idx.


<img width="423" height="232" alt="image" src="https://github.com/user-attachments/assets/2290c0e6-107b-43eb-85d6-444d9b9b2472" />
display = Menampilkan Seluruh Isi Queue
 i = self.front_idx Mulai iterasi dari posisi terdepan
 print(self.q[i], end=" ") Cetak elemen saat ini
if i == self.rear_idx: Berhenti setelah elemen terakhir tercetak
 i = (i + 1) % self.MAXN menggeser indeks ke slot berikutnya secara sirkular
 Loop while True dengan pengecekan if i == self.rear_idx: break dipilih agar bisa menangani kasus ketika rear_idx < front_idx.


<img width="472" height="594" alt="image" src="https://github.com/user-attachments/assets/9f9878b2-a537-4a1c-97a6-a4d70bf2ba76" />
Fungsi main() = Fungsi pengendali utama yang menjalankan.
while pilih != 5: Loop terus berjalan sampai user memilih opsi 5 (Keluar)
pilih = int(input("Pilih: ")) Konversi input ke integer
print("Input tidak valid!") error jika input bukan angka


<img width="213" height="44" alt="image" src="https://github.com/user-attachments/assets/72542912-ad03-432b-bff2-855ad4e9b249" />
memastikan main() hanya dipanggil saat file dijalankan langsung

OUTPUT

<img width="705" height="502" alt="image" src="https://github.com/user-attachments/assets/409aa690-444a-4ccf-820e-9203134645b4" />
<img width="712" height="482" alt="image" src="https://github.com/user-attachments/assets/b6a5aa9a-b415-4af2-92a4-25e6fe97bc29" />
<img width="352" height="462" alt="image" src="https://github.com/user-attachments/assets/51606fbe-b692-4082-89ab-b5897023c93f" />

Link YouTube : https://youtu.be/_JsaZTNl0Xg
