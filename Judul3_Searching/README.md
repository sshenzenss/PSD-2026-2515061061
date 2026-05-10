A. Judul Program

Program Pengecekan Kamar Penginapan

B. Deskripsi Singkat

Program “Program Pengecekan Kamar Penginapan” berfungsi untuk melakukan pengecekan ketersediaan kamar penginapan berdasarkan nomor kamar yang dimasukkan oleh pengguna. Program akan menampilkan daftar kamar yang tersedia, kemudian pengguna diminta memasukkan nomor kamar yang ingin dipesan. Setelah input diterima, program akan mencari apakah nomor kamar tersebut terdapat di dalam data kamar. Jika kamar ditemukan, program akan menampilkan pesan bahwa kamar tersedia beserta posisi indeks kamar tersebut di dalam list data. Jika kamar tidak ditemukan, program akan menampilkan pesan bahwa kamar tidak tersedia dan meminta pengguna memilih kamar lain.

Algoritma struktur data yang diterapkan pada program ini adalah Sequential Search dengan menggunakan struktur data array/list Python. Sequential Search bekerja dengan cara memeriksa data satu per satu secara berurutan dari indeks pertama hingga terakhir sampai data yang dicari ditemukan. Pada program ini, pencarian dilakukan menggunakan perulangan while yang membandingkan setiap elemen list data dengan nilai target yang dimasukkan pengguna.

C. Source Code
<img width="868" height="479" alt="image" src="https://github.com/user-attachments/assets/9365653b-f004-4c2e-84b0-1ffdd1dac425" />
Penjelasan per baris
1. Judul program
2. -
3. Mendefinisikan fungsi sequential search yang memiliki parameter data, n, dan target
4. Inisialisasi variabel i yang bernilai 0 sebagai indeks awal
5. Perulangan selama nilai i kurang dari n
6. Pengondisian jika nilai data pada indeks i sama dengan target
7. Menampilkan “kamar tersedia”
8. Menampilkan kamar yang dipilih ada pada indeks ke berapa pada list array
9. Indeks i bertambah satu untuk mengecek indeks selanjutnya
10. Pengondisian jika target tidak ada di data
11. Menampilkan "Kamar tidak tersedia, silakan pilih kamar lain"
12. Memanggil fungsi main() untuk memulai kembali program
13. -
14. Mendefinisikan fungsi main() sebagai program utama
15. Membuat variabel data yang berisikan nomor kamar bertipe data integer
16. Membuat variabel n yang memiliki nilai jumlah karakter dari variabel data
17. Menampilkan seluruh data kamar yang ada pada variabel data
18. Perulangan selama kondisi True
19. try, Program akan mencoba untuk
20. Meminta input nomor kamar yang diinginkan bertipe data integer dan nilainya disimpan pada variabel target
21. break, untuk keluar dari perulangan
22. except, jika value error ketika input nilai
23. Menampilkan "Input tidak valid, silakan masukkan angka!"
24. Memanggil fungsi sequential_search dengan variabel data, n, dan target
25. -
26. entry point agar program hanya berjalan saat dijalankan

D. Output Program
<img width="740" height="281" alt="image" src="https://github.com/user-attachments/assets/106f0d05-3ec1-45bd-a623-9b14a02e4859" />
Pada output, program menampilkan data kamar yang tersedia dan meminta user untuk menginputkan nomor kamar yang diinginkan. User menginputkan 110 yang dimana kamar tersebut ada pada data kamar yang ditampilkan, maka program menampilkan pesan kamar tersedia dan juga menampilkan posisi indeks dari nomor kamar tersebut di dalam array. Lalu, program pun selesai. Pada percobaan program selanjutnya, user menginputkan 203 yang dimana nomor tersebut tidak ada dalam data kamar yang ditampilkan oleh program, maka program menampilkan pesan bahwa kamar tidak tersedia dan mempersilahkan user untuk memilih kamar lainnya. Lalu, program meminta input kembali nomor kamar yang diinginkan dan diisi 105 oleh user. Nomor tersebut ada pada data kamar sehingga program menampilkan pesan kamar tersedia dan juga menampilkan posisi indeks nomor kamar tersebut di dalam array.

E. Link Video
https://youtu.be/cq9In2OevZ0?si=JvPZtjpnIf65OJDU

F. Tugas Binary Interpolation
<img width="2113" height="2948" alt="Scanned_20260510-1847" src="https://github.com/user-attachments/assets/be57b438-647f-4c54-86ad-65f253015220" />
