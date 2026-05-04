Program Insertion Sort Pengurutan NPM Mahasiswa

Program sederhana ini dibuat menggunakan bahasa Python untuk mengurutkan data NPM Mahasiswa menggunakan algoritma Insertion Sort 
secara ascending (dari terkecil ke terbesar).

Program ini dibuat sebagai implementasi dari algoritma Insertion Sort pada mata kuliah Praktikum Struktur Data. 
Insertion Sort merupakan sebuah teknik pengurutan dengan cara membandingkan dan mengurutkan dua data pertama pada array, kemudian 
membandingkan data para array berikutnya apakah sudah berada di tempat semestinya. 
Algorithma insertion sort seperti proses pengurutan kartu yang berada di tangan kita
Algoritma ini cocok digunakan untuk data berukuran kecil karena sederhana dan mudah dipahami.

SOURCE CODE : INPUT 


<img width="323" height="17" alt="image" src="https://github.com/user-attachments/assets/b0e21a04-25d7-4714-b76a-9818d6c323a0" />
Command berfungsi hanya sebagai keterngan saja diawal codingan


<img width="226" height="21" alt="image" src="https://github.com/user-attachments/assets/693cdab7-b8a0-44d8-8044-cfa4aae7c028" />
Membuat fungsi bernama insertion_sort.
arr : list yang berisi data NPM nantinya
n   : jumlah data NPM yang akan di masukkan


<img width="178" height="24" alt="image" src="https://github.com/user-attachments/assets/02d0e864-8e9d-450a-b818-ed38d9438281" />
Perulangan dimulai dari indeks ke-1 sampai terakhir. 
Karena data pertama yang ke 0 dianggap sudah terurut dengan sendirinya.


<img width="117" height="24" alt="image" src="https://github.com/user-attachments/assets/79df50ba-1e34-45b2-936d-11d65d1e279c" />
Menyimpan nilai sementara yaitu nilai i


<img width="96" height="26" alt="image" src="https://github.com/user-attachments/assets/f53d8bf4-5429-44f2-a1ea-e999d9c44365" />
Variabel j disini digunakan untuk mengecek data sebelumnya.


<img width="249" height="18" alt="image" src="https://github.com/user-attachments/assets/ac001315-fed7-4a6e-a64a-1197ff3e4f43" />
Jadi disini terjadinya looping berlaku selama j masih didalam array dan data di j lebih besar dari temp


<img width="161" height="22" alt="image" src="https://github.com/user-attachments/assets/528524da-0a8d-49eb-afe1-d0482ccb917f" />
Menggeser data yang lebih besar ke kanan ke posisi j+1


<img width="77" height="26" alt="image" src="https://github.com/user-attachments/assets/5b82305e-d189-4510-bdcd-53b15f9ccaf4" />
Mundur satu posisi ke kiri untuk memastikan data berikutnya atau membandingkan


<img width="141" height="21" alt="image" src="https://github.com/user-attachments/assets/02c747a4-6ee1-4e6c-94ed-39b77b5325e9" />
Menaruh nilai temp ke posisi yang benar setelah posisi yang tepat ditemukan


<img width="92" height="17" alt="image" src="https://github.com/user-attachments/assets/d5f51c6e-c451-48e0-b216-8acd82ec09c8" />
membuat fungsi utama dari program


<img width="384" height="97" alt="image" src="https://github.com/user-attachments/assets/9baf92c5-25bb-488f-9b6f-4fb269c410a1" />
Digunakan untuk meminta user memasukan data jumlah mahasiswa.
Jika user memasukkan bukan angka, program akan menampilkan pesan error.


<img width="296" height="41" alt="image" src="https://github.com/user-attachments/assets/edf13b32-a9b4-406a-9672-3795adbdddd0" />
Membuat semacam list kosong untuk menyimpan atau memasukan data NPM Mahasiswa


<img width="142" height="21" alt="image" src="https://github.com/user-attachments/assets/b3f7ef5b-61ea-4758-b89c-9c68a0b6d018" />
Melakukan looping sebanyak data NPM Mahasiswa


<img width="90" height="21" alt="image" src="https://github.com/user-attachments/assets/1b4607ea-b1e8-4176-88e8-409ecd678b9d" />
Terus meminta input ulang jika user memasukkan bukan angka


<img width="175" height="75" alt="image" src="https://github.com/user-attachments/assets/80e84085-6a42-4b64-bb8b-b83ed2796e11" />
Memasukkan data NPM yang valid.
Break berfungsi keluar dari while jika input sudah benar atau valid.

<img width="428" height="37" alt="image" src="https://github.com/user-attachments/assets/9171e0f4-4dec-4f23-9b15-0f6de53b6f16" />
Menampilkan pesan kesalahan atau error jika input yang dimasukkan tidak valid.
 

<img width="414" height="19" alt="image" src="https://github.com/user-attachments/assets/81766d1a-4a59-4066-ad38-00370a6fc46a" />
Menampilkan semua data NPM yang sudah diinput dalam bentuk list, sebelum proses pengurutan dilakukan. 
Berguna untuk membandingkan kondisi data NPM sebelum dan sesudah diurutkan.


<img width="173" height="20" alt="image" src="https://github.com/user-attachments/assets/5ba940ab-92d1-44ec-b3ff-6e025d28c765" />
Berfungsi untuk memanggil fungso insertionnya untuk memulai proses pengurutan


<img width="560" height="22" alt="image" src="https://github.com/user-attachments/assets/a283ff15-4f3d-45ff-8347-c52c9bce9280" />
Menampilkan teks/data hasil sorting dan end=" " berfungsi agar output berikutnya tetap di baris yang sama.


<img width="203" height="59" alt="image" src="https://github.com/user-attachments/assets/f6c72c1a-9bb2-4721-9492-25558a7b48a4" />
for i in range(n) berfungsi menampilkan seluruh data NPM satu per satu
print di akhir pindah baris setelah output selesai ditampilkan


<img width="206" height="42" alt="image" src="https://github.com/user-attachments/assets/f661b251-08a3-4108-b91a-4a9380691d7a" />
Fungsi main() hanya dipanggil ketika file ini dijalankan langsung oleh user



OUTPUT


<img width="211" height="21" alt="image" src="https://github.com/user-attachments/assets/7ee8d569-a32b-4f19-bf0d-cc4af59de8c0" />
User diminta untuk memasukkan jumlah mahasiswa.
Saya memasukkan 4


<img width="692" height="120" alt="image" src="https://github.com/user-attachments/assets/32d8c85a-296c-48f5-ac85-76a575d71dfe" />
Selanjutnya ialah memasukan data NPM tiap Mahasiswa, lalu data tersebut diurutkan dari yang terkecil hingga yang terbesar.



PROGRAM TELAH BERHASIL DAN SELESAI



Link Video YouTube : https://youtu.be/3IbD_bimzxo
