A. JUDUL PROGRAM: Program Data Umur Pasien KIinik

B. DESKRIPSI SINGKAT:

Program tersebut berfungsi sebagai sistem untuk mengelola data umur pasien pada sebuah klinik. Pengguna dapat memasukkan umur pasien, mencari data umur tertentu, menampilkan daftar umur pasien secara terurut dari yang termuda hingga tertua, mengetahui umur pasien paling muda dan paling tua, serta menghitung jumlah seluruh pasien yang tersimpan. Data umur pasien disimpan dalam bentuk tree sehingga proses pencarian dan pengurutan data menjadi lebih efisien dibandingkan penyimpanan biasa menggunakan list.

Struktur data dan algoritma yang diterapkan pada program ini adalah Binary Search Tree (BST). BST merupakan struktur data pohon biner yang memiliki aturan bahwa nilai pada subtree kiri selalu lebih kecil dari root, sedangkan nilai pada subtree kanan selalu lebih besar dari root. Program menerapkan beberapa operasi utama BST seperti insert untuk menambahkan data, search untuk mencari data, inorder traversal untuk menampilkan data secara terurut, find_min untuk mencari nilai terkecil, find_max untuk mencari nilai terbesar, dan count_nodes untuk menghitung jumlah node. Dengan menggunakan BST, proses pencarian dan pengelolaan data dapat dilakukan lebih cepat dan terstruktur.

SOURCE CODE:
![1](image.png)
![2](image-1.png)
![3](image-2.png)
![4](image-3.png)

penjelasan kode per baris
1. Membuat class Node yang digunakan sebagai node pada Binary Search Tree (BST).
2. Constructor class Node yang dijalankan saat object node dibuat.
3. Menyimpan nilai/data node ke variabel key.
4. Pointer child kiri diisi None karena awalnya belum memiliki child kiri.
5. Pointer child kanan diisi None karena awalnya belum memiliki child kanan.
6. -
7. Membuat class utama Binary Search Tree.
8. Constructor class BST.
9. Root tree awalnya kosong.
10. -
11. Fungsi rekursif untuk menambahkan node ke BST.
12. Mengecek apakah posisi node root kosong.
13. Membuat node baru jika posisi kosong.
14. Mengecek apakah nilai lebih kecil dari root.
15. Memasukkan data ke subtree kiri secara rekursif.
16. Mengecek apakah nilai lebih besar dari root.
17. Memasukkan data ke subtree kanan secara rekursif.
18. Mengembalikan root setelah proses insert selesai.
19. -
20. Fungsi insert utama.
21. Memulai insert dari root tree.
22. -
23. Fungsi rekursif untuk mencari data pada BST.
24. Mengecek apakah node kosong.
25. Mengembalikan False jika data tidak ditemukan.
26. Mengecek apakah data ditemukan.
27. Mengembalikan True jika data ditemukan.
28. Mengecek apakah data yang dicari lebih kecil dari root.
29. Mencari data di subtree kiri.
30. Pengondisian terakhir untuk mencari data di subtree kanan.
31. -
32. Fungsi search utama.
33. Memulai pencarian dari root.
34. -
35. Fungsi traversal inorder.
36. Mengecek apakah node root kosong.
37. return untuk menghentikan fungsi jika node kosong.
38. Traversal pada subtree kiri.
39. Mencetak nilai root.
40. Traversal  pada subtree kanan.
41. -
42. Fungsi untuk mencari nilai minimum pada pohon.
43. Mengecek apakah tree kosong.
44. Mengembalikan -1 jika tree kosong.
45. Menyimpan root ke variabel current.
46. Perulangan selama masih ada child kiri.
47. Berpindah ke node paling kiri.
48. Mengembalikan nilai terkecil pada pohon.
49. -
50. Fungsi mencari nilai maksimum.
51. Mengecek apakah tree kosong.
52. Mengembalikan -1 jika tree kosong.
53. Menyimpan root ke variabel current.
54. Perulangan selama masih ada child kanan.
55. Berpindah terus ke node paling kanan.
56. Mengembalikan nilai terbesar pada pohon.
57. -
58. Fungsi menghitung jumlah node.
59. Mengecek apakah node kosong.
60. Mengembalikan 0 jika node kosong.
61. Menghitung jumlah seluruh node menggunakan rekursi.
62. -
63. Fungsi utama program.
64. Membuat object BST.
65. Variabel untuk menyimpan pilihan menu.
66. Perulangan menu selama pengguna belum memilih keluar.
67. Menampilkan judul program.
68. Menampilkan menu masukkan umur pasien.
69. Menampilkan menu cari umur pasien.
70. Menampilkan menu urutkan umur pasien.
71. Menampilkan menu mencari umur termuda.
72. Menampilkan menu mencari umur tertua.
73. Menampilkan menu menghitung jumlah data pasien.
74. Menampilkan menu keluar.
75. Mencoba menjalankan input pilihan.
76. Meminta pengguna memasukkan pilihan menu.
77. Menangani error jika input bukan angka.
78. Menampilkan pesan error.
79. Kembali ke awal perulangan menu.
80. Apabila pengguna memilih menu 1.
81. Mencoba input umur pasien.
82. Meminta input umur pasien yang lalu disimpan pada variabel x.
83. Menambahkan umur pasien ke BST dengan operasi insert.
84. Menampilkan pesan berhasil.
85. Menangani error input.
86. Menampilkan pesan error.
87. Apabila user memilih menu 2.
88. Mencoba input pencarian.
89. Meminta umur pasie yang dicari yang lalu disimpan pada variabel x.
90. Mengecek apakah umur ditemukan.
91. Menampilkan pesan jika ditemukan.
92. Jika data tidak ditemukan.
93. Menampilkan pesan tidak ditemukan.
94. Menangani error input.
95. Menampilkan pesan error.
96. Apabila user memilih menu 3.
97. Menampilkan urutan umur pasien termuda ke tertua.
98. Memanggil fungsi traversal inorder.
99. Membuat baris baru untuk mencetak.
100. Apabila user memilih menu 4.
101. Menampilkan umur pasien termuda.
102. Apabila user memilih menu 5.
103. Menampilkan umur pasien tertua.
104. Apabila user memilih menu 6.
105. Menampilkan jumlah data pasien yang ada pada pohon.
106. Apabila user memilih menu 7.
107. Menampilkan pesan program selesai.
108. Jika pilihan menu yang diinputkan user bukan 1, 2, 3, 4, 5, 6, dan 7.
109. Menampilkan pesan pilihan salah dan tidak valid.
110. -
111. Mengecek apakah file dijalankan langsung.
112. Menjalankan fungsi utama program.

D. OUTPUT PROGRAM:
![1](image-4.png)
![2](image-5.png)
![3](image-6.png)
![4](image-7.png)
![5](image-8.png)

Program menampilkan menu utama data umur pasien klinik. Pengguna kemudian memilih menu nomor 1 untuk memasukkan data umur pasien ke dalam Binary Search Tree (BST). Data umur yang dimasukkan secara berurutan adalah 30, 32, 25, 10, 65, 43, dan 2. Setiap data yang berhasil dimasukkan akan menampilkan pesan “Data berhasil dimasukkan”. Setelah seluruh data tersimpan, pengguna memilih menu nomor 3 untuk menampilkan seluruh umur pasien secara terurut dari yang termuda hingga tertua menggunakan traversal inorder pada BST. Hasil yang ditampilkan adalah 2, 10, 25, 30, 32, 43, dan 65.

Selanjutnya pengguna memilih menu nomor 2 untuk melakukan pencarian umur pasien. Ketika pengguna mencari umur 30, program menampilkan pesan “Pasien ditemukan” karena data tersebut terdapat di dalam BST. Namun saat pengguna mencari umur 7, program menampilkan pesan “Pasien tidak ditemukan” karena data tersebut tidak ada pada tree. Setelah itu pengguna memilih menu nomor 4 untuk mencari umur pasien termuda dan program menampilkan nilai 2 sebagai umur termuda. Pada menu nomor 5, program mencari umur pasien tertua dan menghasilkan nilai 65 sebagai umur tertua. Kemudian pada menu nomor 6, program menghitung jumlah seluruh node atau data pasien yang tersimpan pada BST dan menghasilkan total 7 pasien. Terakhir, ketika pengguna memilih menu nomor 7, program menampilkan pesan “Program selesai” dan perulangan menu dihentikan.

E. Link Video: [youtube](https://youtu.be/E5sSE2suubg)