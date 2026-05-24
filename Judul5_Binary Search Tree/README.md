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
### 1. Class `Node`

```python
class Node:
    def __init__(self, key):
        self.key = key       # Nomor kamar yang disimpan
        self.left = None     # Pointer ke anak kiri (belum ada = None)
        self.right = None    # Pointer ke anak kanan (belum ada = None)
```

**Penjelasan:**
- `class Node` → Mendefinisikan template/cetakan untuk setiap kamar dalam pohon.
- `__init__(self, key)` → Constructor: dijalankan otomatis saat objek Node dibuat.
- `self.key = key` → Menyimpan nomor kamar sebagai nilai node.
- `self.left = None` → Awalnya tidak punya anak kiri.
- `self.right = None` → Awalnya tidak punya anak kanan.

### 2. Class `BSTDasar`

```python
class BSTDasar:
    def __init__(self):
        self.root = None     # Pohon dimulai kosong (belum ada kamar)

    def insert_node(self, root, key):
        if root is None:               # Posisi kosong ditemukan → taruh node baru di sini
            return Node(key)
        if key < root.key:             # Nomor kamar lebih kecil → masuk ke sisi kiri
            root.left = self.insert_node(root.left, key)
        elif key > root.key:           # Nomor kamar lebih besar → masuk ke sisi kanan
            root.right = self.insert_node(root.right, key)
        return root                    # Kembalikan node yang sudah diperbarui

    def insert(self, key):
        self.root = self.insert_node(self.root, key)  # Mulai dari root pohon
```

**Penjelasan:**
- `self.root = None` → Pohon BST dimulai dalam keadaan kosong.
- `insert_node(root, key)` → Fungsi rekursif yang mencari posisi tepat untuk nomor kamar baru.
- `if root is None` → Jika posisi kosong ditemukan, buat node baru di situ.
- `if key < root.key` → Jika nomor kamar lebih kecil, telusuri ke **kiri**.
- `elif key > root.key` → Jika lebih besar, telusuri ke **kanan**.
- Duplikat diabaikan (tidak ada `elif key == root.key`).
- `insert(key)` → Fungsi publik yang memanggil `insert_node` mulai dari akar pohon.

> 💡 **Proses insert kamar nomor 7 ke pohon yang sudah ada 10, 5:**
> 
> `7 < 10` → kiri → `7 > 5` → kanan dari 5 → **ditempatkan di sana!**

---

### 3. Class `BSTDasar` — Fungsi Search

```python
    def search_node(self, root, key):
        if root is None:               # Sampai ujung pohon, kamar tidak ditemukan
            return False
        if root.key == key:            # Kamar ditemukan!
            return True
        if key < root.key:             # Kamar yang dicari lebih kecil → cari ke kiri
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)  # Lebih besar → cari ke kanan

    def search(self, key):
        return self.search_node(self.root, key)   # Mulai pencarian dari root
```

**Penjelasan:**
- `search_node(root, key)` → Fungsi rekursif untuk mencari nomor kamar.
- `if root is None` → Jika sudah mencapai ujung pohon dan belum ketemu → `False`.
- `if root.key == key` → Kamar ditemukan → `True`.
- Logika `kiri/kanan` sama seperti insert, memanfaatkan sifat BST.
- `search(key)` → Fungsi publik yang dipanggil dari menu utama.

> 💡 **Keunggulan BST:** Pencarian jauh lebih cepat dari list biasa. Di pohon dengan 1000 kamar, BST maksimal butuh ~10 langkah (karena log₂1000 ≈ 10).

---

### 4. Class `BSTDasar` — Fungsi Traversal

#### Inorder (Urutan Terurut ↑)
```python
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)       # 1. Kunjungi kiri dulu
        print(root.key, end=" ")      # 2. Cetak nilai saat ini
        self.inorder(root.right)      # 3. Kunjungi kanan
```
> Menghasilkan daftar kamar **dari nomor terkecil ke terbesar** (urut naik).

#### Preorder (Root Lebih Dulu)
```python
    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")      # 1. Cetak nilai saat ini (root dulu)
        self.preorder(root.left)      # 2. Kunjungi kiri
        self.preorder(root.right)     # 3. Kunjungi kanan
```
> Berguna untuk **menyalin/merekonstruksi** pohon BST.

#### Postorder (Root Paling Akhir)
```python
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)     # 1. Kunjungi kiri
        self.postorder(root.right)    # 2. Kunjungi kanan
        print(root.key, end=" ")      # 3. Cetak nilai saat ini (root terakhir)
```
> Berguna untuk **menghapus** pohon secara aman (anak dihapus sebelum induk).

**Perbandingan hasil ketiga traversal pada contoh pohon `10, 5, 15, 3, 7`:**

| Traversal  | Urutan Kunjungan | Hasil Output    |
|------------|------------------|-----------------|
| Inorder    | Kiri → Root → Kanan | `3 5 7 10 15` |
| Preorder   | Root → Kiri → Kanan | `10 5 3 7 15` |
| Postorder  | Kiri → Kanan → Root | `3 7 5 15 10` |

---

### 5. Class `BSTDasar` — Fungsi `count_nodes`

```python
    def count_nodes(self, root):
        if root is None:               # Tidak ada node → kembalikan 0
            return 0
        # 1 (node ini) + jumlah node kiri + jumlah node kanan
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
```

**Penjelasan:**
- Menggunakan rekursi untuk menghitung **semua node** di pohon.
- `if root is None: return 0` → Basis rekursi: pohon kosong = 0 node.
- `1 + kiri + kanan` → Hitung node saat ini ditambah semua node di subtree kiri dan kanan.

> 💡 **Contoh untuk pohon `10, 5, 15, 3, 7`:**
> 
> count(10) = 1 + count(5) + count(15)
>           = 1 + (1 + count(3) + count(7)) + (1 + 0 + 0)
>           = 1 + (1 + 1 + 1) + 1 = **5** ✓

---

### 6. Fungsi `main()` — Menu Utama

```python
def main():
    bst = BSTDasar()    # Buat pohon BST baru yang kosong
    pilih = 0

    while pilih != 7:   # Ulangi terus sampai user memilih menu 7 (Keluar)
        # Tampilkan menu...
        print("\nManajemen Kamar Kosan")
        print("1. Masukkan Kamar Kos yang Tersedia")
        # ...dst

        try:
            pilih = int(input("Pilih menu: "))   # Baca input user, konversi ke integer
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue   # Kembali ke awal loop jika input bukan angka

        if pilih == 1:       # INSERT kamar baru
            x = int(input("Masukkan Nomor Kamar: "))
            bst.insert(x)

        elif pilih == 2:     # SEARCH kamar
            x = int(input("Cari Nomor Kamar: "))
            if bst.search(x):
                print(f"Kamar No {x} Tersedia.")
            else:
                print(f"Kamar No {x} Tidak Tersedia.")

        elif pilih == 3:     # Tampilkan INORDER
            bst.inorder(bst.root)

        elif pilih == 4:     # Tampilkan PREORDER
            bst.preorder(bst.root)

        elif pilih == 5:     # Tampilkan POSTORDER
            bst.postorder(bst.root)

        elif pilih == 6:     # Hitung TOTAL kamar
            print(f"Total ada {bst.count_nodes(bst.root)} kamar.")

        elif pilih == 7:     # KELUAR dari program
            print("Sistem Selesai")
```

**Penjelasan:**
- `bst = BSTDasar()` → Membuat objek pohon BST yang siap dipakai.
- `while pilih != 7` → Program terus berjalan sampai user memilih keluar.
- `try/except ValueError` → **Error handling** — jika user salah input huruf, program tidak crash.
- `continue` → Kembali ke awal loop, tampilkan menu lagi.
- `if __name__ == "__main__": main()` → Memastikan fungsi `main()` hanya dijalankan jika file ini dieksekusi langsung (bukan di-import sebagai modul).

---

## ▶ Cara Menjalankan

Pastikan Python 3 sudah terinstal, lalu jalankan:

```bash
python bst_kosan.py
```

---

## 📋 Contoh Penggunaan

```
Manajemen Kamar Kosan
1. Masukkan Kamar Kos yang Tersedia
2. Cek Ketersediaan Kamar
...

Pilih menu: 1
Masukkan Nomor Kamar yang Tersedia: 10
Kamar nomor 10 berhasil didaftarkan ke sistem!

Pilih menu: 1
Masukkan Nomor Kamar yang Tersedia: 5
Kamar nomor 5 berhasil didaftarkan ke sistem!

Pilih menu: 2
Cari Nomor Kamar: 5
Kamar No 5 Tersedia.

Pilih menu: 3
Daftar Kamar (Inorder): 5 10
```

---

