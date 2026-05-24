# Sistem Manajemen Kamar Kosan

Sebuah program sederhana berbasis Pythonuntuk mengelola kamar kosan menggunakan struktur data Binary Search Tree (BST).

---

**Binary Search Tree (BST)** adalah struktur data pohon biner di mana:
- Setiap **node** memiliki maksimal **2 anak** (kiri dan kanan).
- Node di **kiri** selalu memiliki nilai **lebih kecil** dari node induknya.
- Node di **kanan** selalu memiliki nilai **lebih besar** dari node induknya.
---


## SOURCE CODE :

## INPUT
# Class `Node`
<img width="231" height="104" alt="image" src="https://github.com/user-attachments/assets/94caa21d-9e77-4541-85d6-7b6586024d37" />

sebuah kelas bernama Node untuk membuat struktur dasar penyimpan data.
Pada line ke 3 dijalankan otomatis saat objek Node dibuat.
Line ke 4 digunakan untuk menyimpan nomor kamar sebgai nilai node
Pada line ke 5 dan ke 6 itu ialah sebuah fungsi pointer untuk ke anak kiri dan kanan

# Class `BSTDasar`
<img width="465" height="295" alt="image" src="https://github.com/user-attachments/assets/71ce89f9-ff62-4a79-b08d-d3c711293d45" />

Pada line 9 Terdapat deklarasi sebuah kelas bernama BSTDasar sebagai inti dari struktur Binary Search Tree.
self.root = None Menunjukkan Tree BST dimulai dalam keadaan kosong
insert_node(root, key) ialah Fungsi untuk mencari posisi tepat untuk nomor kamar baru.
if root is None  Posisi kosong untuk membuat node baru
if key < root.key : Jika nomor kamar lebih kecil, telusuri ke kiri.
elif key > root.key : Jika lebih besar, telusuri ke kanan.
insert(key) ialah Fungsi yang memanggil insert_node mulai dari akar pohon.

# Fungsi Search
<img width="372" height="217" alt="image" src="https://github.com/user-attachments/assets/45bb1355-9971-4d07-bcd9-be2923bc6854" />
search_node(root, key) : Sebuah fungsi untuk mencari nomor kamar.
if root is None : Jika sudah mencari sampe ujung pohon dan kamar gak ketemu = False.
if root.key == key : Kamar ditemukan = True.
pada def search disitu Memulai pencarian dari root

# Inorder
<img width="222" height="121" alt="image" src="https://github.com/user-attachments/assets/6aea321b-54a7-4853-a302-cc58a45b0293" />

Fungsi menghasilkan daftar kamar dari nomor terkecil ke terbesar (urut naik).
Urutannya Mengecek bagian kiri dulu, lalu ke root, dan terakhir mengecek bagian kanan

# Preorder
<img width="242" height="118" alt="image" src="https://github.com/user-attachments/assets/71c335e3-ba02-4d1e-9681-fa3720f6f01b" />

Urutannya pengecekannya dari root langsung di ambil, lalu cek bagian kiri, dan terakhir mengecek bagian kanan

# Postorder
<img width="244" height="120" alt="image" src="https://github.com/user-attachments/assets/2c4dfa85-6dc1-4d7e-8937-1c992fab0f45" />

Dengan urutan pengecekan dimulai dari bagian kiri, lalu ke kanan, dan barulah ke bagian root

# Count Nodes
<img width="570" height="82" alt="image" src="https://github.com/user-attachments/assets/769dadea-57df-444d-b0d4-14331271614c" />

Fungsi ini digunakan untuk menghitung semua node di tree.
Jadi fungsi ini menghitung node saat ini ditambah semua node di subtree kiri dan kanan.

# Fungsi Main(Utama)
<img width="433" height="348" alt="image" src="https://github.com/user-attachments/assets/f37b2e06-23f4-4b33-b11e-61d2f27b8437" />

Berisi perintah untuk membuat tree baru kosong (bst = BSTDasar()) dan berisi menu output 1 sampai 7 opsi
Dibawah menu output ada fungsi untuk membaca input user dan memaksa user memasukan intut berbentuk angka

<img width="590" height="609" alt="image" src="https://github.com/user-attachments/assets/c99c2b63-5aa6-416a-951e-2c3e522a1b33" />
<img width="593" height="150" alt="image" src="https://github.com/user-attachments/assets/33f05e35-40b1-4571-8c0e-46a7d92ad059" />








