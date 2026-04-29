Program Implementasi Sederhana lispt Data Nilai Mahasiswa

Program ini merupakan implementasi sederhana pengelolaan data nilai mahasiswa menggunakan struktur data list (array 1 dimensi) pada bahasa pemrograman Python.
Melalui menu interaktif yang disediakan, pengguna dapat melihat alamat memori (address) darivariabel list secara keseluruhan, mengecek address dari masing-masing
indeks elemen di dalamnya, serta menginputkan lima data nilai mahasiswa yang kemudian akan langsung ditampilkan ke layar.

Dalam penerapannya, program ini menggunakan beberapa konsep dasar pemrograman seperti fungsi, perulangan (while dan for), serta percabangan (if-elif-else)
untuk mengatur alur aplikasi. Selain itu, program juga telah dilengkapi dengan fitur exception handling (try-except) untuk memvalidasi input.
Hal ini memastikan pengguna hanya memasukkan tipe data angka (integer), sehingga program terhindar dari error dan dapat terus berjalan jika terjadi kesalahan input

source code : 

INPUT

<img width="438" height="118" alt="image" src="https://github.com/user-attachments/assets/0455b537-8ca8-43e7-bb60-507cb37ab15f" />
Fungsi ini bertugas menampilkan menu pilihan ke layar setiap kali program meminta input dari
pengguna. Tidak menerima parameter apapun dan hanya berfungsi sebagai tampilan antarmuka.

<img width="182" height="58" alt="image" src="https://github.com/user-attachments/assets/53d5872e-6cf8-4436-bc7d-006d67eacefb" />
line pertama membuat list berisi 5 elemen dengan nilai awal 0.
Ini adalah deklarasi array 1 dimensi berkapasitas 5.
line kedua pada foto variabel kontrol untuk menjaga program tetap berjalan
selama belum memilih keluar.

<img width="350" height="115" alt="image" src="https://github.com/user-attachments/assets/267ed869-2570-4b84-95e9-acc5a869376e" />
Program berjalan dalam loop while selama running bernilai True. Setiap iterasi
menampilkan menu lalu meminta input pilihan. Blok try-except digunakan untuk menangani
jika pengguna memasukkan bukan angka, sehingga program tidak crash dan langsung meminta
input ulang dengan continue.

<img width="457" height="39" alt="image" src="https://github.com/user-attachments/assets/9583b77d-fa77-4b70-80ea-b70d50a996f3" />
Menampilkan alamat memori dari list nilai secara keseluruhan menggunakan fungsi id().
Address yang muncul adalah lokasi di memori tempat list tersebut disimpan.

<img width="430" height="59" alt="image" src="https://github.com/user-attachments/assets/619c22fc-d1d2-4bf7-833c-1966f4516467" />
Melakukan iterasi sebanyak 5 kali untuk menampilkan alamat memori dari setiap elemen
list. Perlu diperhatikan bahwa elemen dengan nilai yang sama akan menunjuk ke
address yang sama, karena Python melakukan integer caching untuk nilai kecil.

<img width="480" height="191" alt="image" src="https://github.com/user-attachments/assets/53c12afe-440a-4369-8c26-312ca3ee7b98" />
Program meminta input nilai satu per satu untuk setiap index (0–4). Looping while True
di dalam memastikan jika input bukan angka, program tidak berpindah ke index berikutnya
dan meminta input ulang. Setelah semua terisi, list ditampilkan seluruhnya.

<img width="320" height="109" alt="image" src="https://github.com/user-attachments/assets/1136002b-9d49-421a-b56c-3d549f99726c" />
Jika memilih 4, variabel running diubah menjadi False sehingga loop while
berhenti dan program berakhir. Jika input di luar 1–4, program menampilkan pesan
pilihan tidak valid.

<img width="241" height="49" alt="image" src="https://github.com/user-attachments/assets/367f3111-65bf-4191-bdf0-22f951e7fc4f" />
Standar Python untuk memastikan fungsi main() hanya dijalankan saat file ini
dieksekusi langsung, bukan saat diimport sebagai modul.

OUTPUT

<img width="335" height="125" alt="image" src="https://github.com/user-attachments/assets/93340d00-c186-4959-a3ab-9270d5970c71" />

<img width="314" height="191" alt="image" src="https://github.com/user-attachments/assets/a345573b-3e4e-41b8-9e6e-cc3842c25763" />

<img width="325" height="139" alt="image" src="https://github.com/user-attachments/assets/08937603-e294-4001-bf70-32ba2d93117b" />
Diminta untuk memasukan 5 nilai mahasiswa (0-4)

<img width="331" height="274" alt="image" src="https://github.com/user-attachments/assets/93313f55-a6b2-4934-9316-5d960914ac54" />
Program Selesai

Link Video Youtube : https://youtu.be/Wl86ZDrvrJY?si=kM_wGJVFmJSToh0x
