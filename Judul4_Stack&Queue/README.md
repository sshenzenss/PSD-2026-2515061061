A. JUDUL PROGRAM

Program Antrian Nasabah Bank

B. DESKRIPSI SINGKAT

Program tersebut merupakan sebuah simulasi sistem antrian nasabah bank yang dibuat menggunakan bahasa Python. Program ini memungkinkan pengguna untuk menambahkan nasabah ke dalam antrian, memanggil nasabah sesuai urutan kedatangan, melihat nasabah yang berada di posisi paling depan, serta menampilkan seluruh isi antrian. Setiap nasabah akan mendapatkan nomor antrian secara otomatis sesuai urutan kedatangan. Program berjalan secara interaktif menggunakan menu pilihan sehingga pengguna dapat mengelola antrian dengan mudah. 

Struktur data yang diterapkan pada program ini adalah Queue (antrian) dengan metode implementasi Linked List. Queue bekerja menggunakan prinsip FIFO (First In First Out), yaitu data yang pertama masuk akan menjadi data pertama yang keluar. Pada implementasinya, program menggunakan class Node untuk menyimpan data dan pointer menuju node berikutnya, sedangkan class QueueLinkedList digunakan untuk mengatur operasi-operasi queue seperti enqueue, dequeue, peek, dan display. Penggunaan linked list membuat proses penambahan dan penghapusan data menjadi lebih efisien karena tidak perlu menggeser elemen seperti pada array.

C. Source Code
<img width="835" height="514" alt="image" src="https://github.com/user-attachments/assets/ea5e95d7-cb32-4e71-875e-58389ba6311e" />
<img width="830" height="515" alt="image" src="https://github.com/user-attachments/assets/5f9e081c-5b20-480a-accf-589bfd181603" />
<img width="833" height="511" alt="Cuplikan layar 2026-05-18 182356" src="https://github.com/user-attachments/assets/45b1d78f-d780-4b1d-a844-665ad17c0c6e" />
Penjelasan kode per baris
1. Judul program.
2. -
3. Membuat class Node yang digunakan sebagai elemen pada linked list.
4. Constructor untuk menginisialisasi object node.
5. Menyimpan data ke dalam node.
6. Membuat pointer next awalnya kosong.
7. -
8. Membuat class queue menggunakan linked list.
9. Constructor untuk queue.
10. Pointer untuk menunjukkan elemen paling depan antrian.
11. Pointer untuk menunjukkan elemen paling belakang antrian.
12. Membuat nomor antrian dimulai dari 1.
13. -
14. Fungsi untuk mengecek apakah antrian kosong.
15. Mengembalikan nilai jika antrian kosong.
16. -
17. Fungsi untuk menambahkan data “x” ke belakang antrian.
18. Membuat node baru berisi data “x”.
19. Mengecek apakah antrian kosong.
20. Jika antrian kosong, node baru berada depan antrian.
21. Jika antrian kosong, node baru berada di belakang antrian juga.
22. Pengondisian jika antrian tidak kosong.
23. Node belakang lama menjadi node baru.
24. Pointer belakang dipindahkan ke node baru.
25. Memisahkan data tuple menjadi nomor antrian dan nama berisi nilai “x”.
26. Menampilkan pesan bahwa data berhasil ditambahkan.
27. -
28. Fungsi untuk mengambil antrian paling depan.
29. Mengecek apakah antrian kosong.
30. Jika kosong, tampilkan pesan “antrian kosong”.
31. return, mengembalikan nilai dan keluar dari pengondisian.
32. Menyimpan node paling depan sementara ke variabel temp.
33. Menyimpan variabel temp.data ke no_antrian dan nama.
34. Menampilkan nomor antrian dan nama nasabah yang dipanggil.
35. Pointer depan dipindahkan ke node setelahnya.
36. Mengecek apakah antrian menjadi kosong.
37. Jika kosong, pointer belakang dikosongkan.
38. -
39. Fungsi untuk melihat antrian paling depan tanpa menghapusnya.
40. Mengecek apakah antrian kosong.
41. Jika kosong tampilkan pesan “antrian kosong”.
42. Mengembalikan dan keluar dari pengondisian.
43. Mengambil data no_antrian dan nama dari antrian paling depan.
44. Menampilkan nomor antrian dan nama nasabah terdepan.
45. -
46. Fungsi untuk menampilkan semua antrian.
47. Mengecek apakah antrian kosong.
48. Jika kosong tampilkan pesan “antrian kosong”.
49. Mengembalikan nilai dan keluar dari pengondisian.
50. Menampilkan daftar urutan antrian.
51. Membuat variabel current yang berisi antrian paling depan.
52. Perulangan yang berjalan selama node ada.
53. Menampilkan data current setiap node.
54. Variabel current diubah menjadi node berikutnya.
55. Menampilkan semua data yang ada.
56. -
57. Membuatt fungsi main() sebagai program utama.
58. Membuat variabel queue yang memanggil class QueueLinkedList.
59. Membuat variabel pilih yang memiliki nilai awal 0.
60. Perulangan yang berjalan selama nilai yang diinputkan bukan 5.
61. Menampilkan judul menu.
62. Menampilkan pilihan menu nomor 1.
63. Menampilkan pilihan menu nomor 2.
64. Menampilkan pilihan menu nomor 3.
65. Menampilkan pilihan menu nomor 4.
66. Menampilkan pilihan menu nomor 5.
67. try, program mencoba untuk menerima inputan user.
68. Menerima input pilihan user yang dikonversikan ke tipe data integer.
69. Jika input bukan angka dan terjadi error.
70. Menampilkan pesan error bahwa input tidak valid
71. continue, lanjut ke menu awal
72. Jika user memilih menu nomor 1.
73. Meminta input nama nasabah yang disimpan di variabel nama.
74. Nomor antrian diubah menjadi ke antrian berikutnya.
75. Nomor antrian ditambah satu untuk lanjut ke nasabah berikutnya.
76. Memasukkan data no_antrian dan nama yang diinputkan ke antrian.
77. Jika user memilih menu nomor 2.
78. Memanggil fungsi dequeue() ke antrian.
79. Jika user memilih menu nomor 3.
80. Memanggil fungsi peek() ke antrian.
81. Jika user memilih menu nomor 4.
82. Memanggil fungsi display() ke antrian.
83. Jika user memilih menu nomor 5.
84. Perulangan yang berjalan selama antrian tidak kosong.
85. Memanggil fungsi dequeue() untuk mengeluarkan antrian dari yang paling depan.
86. Menampilkan pesan bahwa program telah selesai.
87. Pengondisian jika input yang diterima adalah selain pilihan menu.
88. Menampilkan pesan bahwa pilihan tidak valid.
89. -
90. Memastikan program dijalankan langsung, bukan di-import.
91. Memanggil fungsi utama program

D. Output Program
<img width="833" height="511" alt="Cuplikan layar 2026-05-18 182356" src="https://github.com/user-attachments/assets/8d267c2a-e30f-4374-a2b6-cf7931a63732" />
<img width="833" height="511" alt="Cuplikan layar 2026-05-18 182356" src="https://github.com/user-attachments/assets/fff0ee49-6138-4b38-b9ae-ae2e794f810f" />
<img width="916" height="335" alt="Cuplikan layar 2026-05-17 130941" src="https://github.com/user-attachments/assets/bb6aa407-2204-4af1-b4b3-ef223f150f0d" />

Program antrian nasabah bank berjalan sesuai konsep struktur data queue dengan metode FIFO (First In First Out). Pada awal program, user memilih menu “Tambahkan ke Antrian” lima kali dan memasukkan nama nasabah, yaitu marko, mei, john, martin, dan nara. Program secara otomatis memberikan nomor antrian mulai dari 1 hingga 5 sesuai urutan input. Setelahnya, user memilih menu “Tampilkan Antrian”. Program kemudian menampilkan seluruh isi queue sesuai urutan kedatangan, yaitu (1, 'marko'), (2, 'mei'), (3, 'john'), (4, 'martin'), dan (5, 'nara').

Selanjutnya, user memilih menu “Panggil dari Antrian”. Nasabah pertama, yaitu marko dengan nomor antrian 1, dipanggil dan dihapus dari antrian. Karena queue menggunakan prinsip FIFO, maka data berikutnya yang ada di posisi terdepan adalah mei dengan nomor antrian 2.  Oleh karena itu, saat pengguna memilih menu “Lihat Antrian Paling Depan”, program menampilkan antrian paling depan sekarang adalah nomor 2, yaitu mei. Selanjutnya, user memilih menu “Kosongkan Antrian dan Keluar”. Nasabah yang tersisa dipanggil sesuai urutan. Lalu, program menampilkan pesan “Program selesai.” dan berhenti dijalankan.

E. Link Video

https://youtu.be/LH6Ha932eUk
