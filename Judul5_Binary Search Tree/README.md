# Sistem Manajemen Kamar Kosan

Sebuah program sederhana berbasis Pythonuntuk mengelola kamar kosan menggunakan struktur data Binary Search Tree (BST).

---

**Binary Search Tree (BST)** adalah struktur data pohon biner di mana:
- Setiap **node** memiliki maksimal **2 anak** (kiri dan kanan).
- Node di **kiri** selalu memiliki nilai **lebih kecil** dari node induknya.
- Node di **kanan** selalu memiliki nilai **lebih besar** dari node induknya.
---


## SOURCE CODE :

# INPUT
### Class `Node`
<img width="231" height="104" alt="image" src="https://github.com/user-attachments/assets/94caa21d-9e77-4541-85d6-7b6586024d37" />
sebuah kelas bernama Node untuk membuat struktur dasar penyimpan data.
Pada line ke 3 dijalankan otomatis saat objek Node dibuat.
Line ke 4 digunakan untuk menyimpan nomor kamar sebgai nilai node
Pada line ke 5 dan ke 6 itu ialah sebuah fungsi pointer untuk ke anak kiri dan kanan

### Class `BSTDasar`
<img width="465" height="295" alt="image" src="https://github.com/user-attachments/assets/71ce89f9-ff62-4a79-b08d-d3c711293d45" />
Pada line 9 Terdapat deklarasi sebuah kelas bernama BSTDasar sebagai inti dari struktur Binary Search Tree.
self.root = None Menunjukkan Tree BST dimulai dalam keadaan kosong
insert_node(root, key) ialah Fungsi untuk mencari posisi tepat untuk nomor kamar baru.
if root is None  Posisi kosong untuk membuat node baru
if key < root.key : Jika nomor kamar lebih kecil, telusuri ke kiri.
elif key > root.key : Jika lebih besar, telusuri ke kanan.
insert(key) ialah Fungsi yang memanggil insert_node mulai dari akar pohon.

## Fungsi Search
<img width="372" height="217" alt="image" src="https://github.com/user-attachments/assets/45bb1355-9971-4d07-bcd9-be2923bc6854" />


