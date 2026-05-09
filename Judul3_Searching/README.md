Implementasi Program Sequential Searching Buku
Program ini mengimplementasikan algoritma Sequential Search (Pencarian Berurutan) menggunakan bahasa pemrograman Python. Program mensimulasikan pencarian nama buku 
di dalam sebuah tas berdasarkan input pengguna.
Sequential Search bekerja dengan cara memeriksa data satu per satu secara berurutan dari awal hingga akhir.

SOURCE KODE :

INPUT

<img width="159" height="15" alt="image" src="https://github.com/user-attachments/assets/4125710a-b6c4-4ac6-8c32-00f14798c4d1" />
Command diawal untuk penamaan kode saja bersifat opsional

<img width="313" height="24" alt="image" src="https://github.com/user-attachments/assets/490245cb-6639-4527-ad12-533673bd8889" />
Mendefinisikan fungsi bernama sequential_search dengan tiga parameter yang pertama ada data ialah list/array yang berisi kumpulan data buku, 
lalu n ialah jumlah total elemen dalam list data, dan target = nama buku yang ingin dicari

<img width="56" height="23" alt="image" src="https://github.com/user-attachments/assets/34f8bc8a-1117-440e-b235-427cd0d22d98" />
deklarasikan variabel i sebagai indeks awal penelusuran, dimulai dari 0 elemen pertama dalam list

<img width="98" height="19" alt="image" src="https://github.com/user-attachments/assets/dbda41da-12fa-458d-8f76-3b7f5f10660a" />
counter sebagai penghitung kemunculan. Variabel ini akan bertambah setiap kali target ditemukan dalam list.

<img width="100" height="23" alt="image" src="https://github.com/user-attachments/assets/99a5d8f6-b6ba-4683-98e7-8bbaa3a4e269" />
Memulai perulangan while yang akan terus berjalan selama nilai i masih kurang dari n (jumlah total data). 
Ini memastikan setiap elemen diperiksa satu per satu dari awal hingga akhir ya sesuai Sequential Search

<img width="168" height="20" alt="image" src="https://github.com/user-attachments/assets/0f203f1f-5bd3-47be-9243-98de5e011b20" />
Memeriksa apakah elemen pada indeks ke i dalam list data sama persis dengan nilai target yang dicari.

<img width="107" height="22" alt="image" src="https://github.com/user-attachments/assets/81f3698a-1135-4954-bfba-691fb4c8e86c" />
Jika kondisi di atas terpenuhi (cocok), maka nilai counter ditambah 1. Ini mencatat bahwa target ditemukan satu kali.

<img width="63" height="23" alt="image" src="https://github.com/user-attachments/assets/08b7e550-2197-4da3-bc91-aa447d7f7b1e" />
Menambah nilai i sebesar 1 untuk berpindah ke elemen berikutnya dalam list pada iterasi berikutnya.

