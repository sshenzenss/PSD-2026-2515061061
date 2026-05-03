A. Judul Program
\nProgram Mengurutkan Nilai IPK Mahasiswa

B. Deskripsi Singkat
\n“Program Mengurutkan nilai IPK Mahasiswa” berfungsi untuk mengelola data mahasiswa yang terdiri atas nama dan IPK. Kemudian, data tersebut diurutkan  berdasarkan nilai IPK. Pengguna diminta untuk memasukkan jumlah mahasiswa serta data masing-masing mahasiswa, lalu program akan menyimpan data tersebut dalam bentuk list berisi tuple (nama, ipk). Setelah itu, program menampilkan data sebelum diurutkan dan melakukan proses pengurutan menggunakan Exchange Sort sehingga menghasilkan daftar mahasiswa dengan IPK yang berurutan dari yang tertinggi ke terendah.
Teknik sorting yang diterapkan dalam program ini adalah Exchange Sort dengan menggunakan struktur data list satu dimensi. Exchange Sort bekerja dengan cara membandingkan elemen dengan seluruh elemen lainnya, kemudian menukar posisi elemen jika ditemukan urutan yang tidak sesuai. Dalam program ini, perbandingan difokuskan pada elemen kedua dari tuple, yaitu IPK. Proses ini dilakukan secara berulang hingga seluruh data tersusun rapi sesuai pengurutan yang diinginkan.

C. Source Code
<img width="1723" height="452" alt="Cuplikan layar 2026-05-02 212515" src="https://github.com/user-attachments/assets/9f898754-b6e2-4e8d-85f3-bc3b6e1703dc" />
<img width="1721" height="981" alt="Cuplikan layar 2026-05-02 212240" src="https://github.com/user-attachments/assets/bd8f9783-a5dd-4876-b753-283013f754d6" />

Penjelasan kode per baris
1. Mendefinisikan fungsi tukar() yang memiliki parameter dataMahasiswa, i, dan j
2. Menyimpan nilai sementara pada indeks i ke variabel temp
3. Mengganti isi indeks i dengan elemen pada indeks j
4. Mengisi indeks j dengan nilai yang sebelumnya disimpan di variabel temp
5. -
6. Mendefinisikan fungsi exchange_sort() yang memiliki dua parameter, yaitu dataMahasiswa dan n
7. Melakukan perulangan luar dengan range (n-1) 
8. Perulangan dalam dari indeks setelah i hingga akhir list
9. Pengondisian dengan membandingkan nilai IPK yang ada di index 1 pada tuple, jika IPK lebih kecil dari pada IPK j
10. Memanggil fungsi tukar() jika kondisi diatas terpenuhi
11. -
12. Mendefinisikan fungsi main() sebagai program utama
13. try, program akan mencoba untuk
14. Menerima input jumlah mahasiswa yang bernilai integer dan disimpan di variabel n
15. except, jika terjadi error saat menerima input
16. Program meminta untuk memasukkan input yang valid
17. return, program berhenti dan kembali ke awal
18. Membuat list dataMahasiswa yang berupa list kosong
19. Perulangan sebanyak jumlah mahasiswa yang diinput
20. Perulangan yang berjalan selama kondisi True
21. try, program akan mencoba untuk
22. Menerima input nama mahasiswa yang disimpan pada variabel nama
23. Menerima input ipk yang bertipe data float dan disimpan pada variabel ipk
24. Pengondisian jika ipk yang diinputkan lebih kecil dari 0 atau lebih besar dari 4
25. Program akan menampilkan pesan untuk ketentuan nilai IPK
26. continue, melanjutkan program dan mengulang input
27. Memasukkan nama dan ipk yang sudah diinputkan ke list dataMahasiswa menggunakan operasi append
28. break, keluar dari loop saat input sudah valid
29. except, saat terjadi error ketika program menerima input
30. Program akan menampilkan pesan untuk memasukkan input yang valid
31. continue, program akan berlanjut dan mengulang input
32. Menampilkan seluruh data mahasiswa sebelum diurutkan
33. Memanggil fungsi Exchange Sort untuk mengurutkan data berdasarkan IPK
34. Menampilkan data setelah diurutkan menggunakan fungsi Exchange Sort tanpa pindah baris karena end = “ ”
35. Perulangan untuk setiap nama dan ipk pada dataMahasiswa menggunakan operasi enumerate
36. Menampilkan nomor urut, nama, dan ipk mahasiswa setelah diurutkan menggunakan exchange sort
37. -
38. entry point program
39. menjalankan fungsi main() sebagai program utama

D. Output Program
<img width="1507" height="856" alt="Cuplikan layar 2026-05-02 221351" src="https://github.com/user-attachments/assets/aaf3ba10-4ea6-4857-8bd0-28c97dcd2244" />

Pada output, program meminta jumlah mahasiswa yang ingin diinputkan dan diisi 3 oleh pengguna. Mahasiswa pertama yang diinputkan adalah putri dengan nilai IPK 3.4. Mahasiswa kedua adalah raka dengan nilai IPK 3.7. Kemudian, mahasiswa yang ketiga adalah nial dengan nilai IPK 4. Selanjutnya, program menampilkan data mahasiswa yang sudah diinputkan oleh pengguna sebelum diurutkan. Setelah itu, program menampilkan data yang sudah diurutkan menggunakan exchange sort. Nial dengan nilai IPK tertinggi berada di posisi pertama, dilanjutkan dengan raka di posisi kedua dan putri di posisi ketiga.

E. Link YouTube
\nhttps://www.youtube.com/watch?v=LEZLLrPFkxE
