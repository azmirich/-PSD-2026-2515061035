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

<img width="129" height="26" alt="image" src="https://github.com/user-attachments/assets/c70f1504-0bb7-467e-8264-6e03d50ab94f" />
Mengembalikan nilai counter (total berapa kali targetnya ditemukan) sebagai hasil dari fungsi ini.

<img width="102" height="30" alt="image" src="https://github.com/user-attachments/assets/1d3d5b15-bab7-4d3f-a500-667562352441" />
Mendefinisikan fungsi utama main() sebagai titik awal masuk program.

<img width="969" height="25" alt="image" src="https://github.com/user-attachments/assets/1709f347-380e-48fd-8827-ada0e87dfc2d" />
Mendeklarasikan variabel data berupa list yang berisi 6 elemen string nama-nama buku yang ada di dalam tas.

<img width="112" height="25" alt="image" src="https://github.com/user-attachments/assets/8e754375-3e0d-4a31-a81c-551bdf4e05e0" />
Menghitung dan menyimpan jumlah total elemen dalam list data menggunakan fungsi bawaan len().

<img width="283" height="25" alt="image" src="https://github.com/user-attachments/assets/b05a4338-96a9-425c-8f84-b98315dc6320" />
Menampilkan isi list data ke output agar user dapat melihat daftar buku yang tersedia sebelum melakukan pencarian.

<img width="101" height="20" alt="image" src="https://github.com/user-attachments/assets/a155c989-d57d-43f2-b7ec-92758a23120c" />
Memulai perulangan tak terbatas (True).

<img width="40" height="20" alt="image" src="https://github.com/user-attachments/assets/ba179da7-8de5-4cf1-9e72-6df4cf7864e8" />
try ini fungsinya kek untuk menangkap error yang mungkin terjadi saat menerima input dari pengguna.

<img width="442" height="22" alt="image" src="https://github.com/user-attachments/assets/edeb3915-0ead-424b-8dec-15b8a46397e0" />
Menampilkan text ke layar dan membaca input dari pengguna, lalu menyimpannya ke variabel target. Nilai elemen inilah yang akan dicari dalam list data buku nantinya.

<img width="52" height="21" alt="image" src="https://github.com/user-attachments/assets/a0c70860-a2f8-41e0-8df1-64f651af2a20" />
Berhenti/keluar dari perulangan while True setelah input berhasil diterima.

<img width="245" height="40" alt="image" src="https://github.com/user-attachments/assets/3d88fbb3-fe76-4601-ba84-a6019e65a446" />
Jika terjadi error saat proses input, program akan mencetak output kesalahan dan perulangan akan kembali meminta input dari awal.

<img width="344" height="19" alt="image" src="https://github.com/user-attachments/assets/9da3453a-b412-48d7-a1d4-2d17a9d3e97e" />
Memanggil fungsi sequential_search dengan data, n, dan target.

<img width="501" height="41" alt="image" src="https://github.com/user-attachments/assets/b1835141-c656-47ed-864c-a81686675285" />
Memeriksa apakah counter lebih dari nol. Jika ya, berarti buku ditemukan dan program mengeprint nama buku beserta jumlah kemunculannya.

<img width="373" height="47" alt="image" src="https://github.com/user-attachments/assets/c1e90f12-3f71-4aef-a54e-b79c049bb352" />
Ini opsi output lain ketika buku tidak ditemukan dalam list dan program mwengeprint output bahwa buku tersebut tidak ada.

<img width="214" height="45" alt="image" src="https://github.com/user-attachments/assets/73b76a93-7272-4ee1-9053-29c3bb9be432" />
Kondisi ini memastikan fungsi main() hanya dipanggil ketika file dijalankan secara langsung (basic python).

OUTPUT

<img width="966" height="42" alt="image" src="https://github.com/user-attachments/assets/7a4d663d-579e-4fd1-aaa3-84ebbbdd5ad0" />
Program meminta user untuk memasukan nama buku/target yang dicari

<img width="405" height="39" alt="image" src="https://github.com/user-attachments/assets/bd3a7fc8-88fe-431d-8963-6446dce35f22" />
Tampilan output buku/target ditemukan

Link Video YouTube : https://youtu.be/WvPIqg2g1xQ

