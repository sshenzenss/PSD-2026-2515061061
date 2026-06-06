A. Judul Program

Program Stok Minuman

B. Deskripsi Singkat

Program ini berfungsi sebagai sistem manajemen stok minuman yang memungkinkan pengguna untuk menambah, mencari, menghapus, dan menampilkan data minuman berdasarkan kode uniknya. Setiap data minuman disimpan dalam bentuk pasangan kunci berupa kode minuman dan nilai berupa nama minuman. Sistem ini mempermudah pencatatan dan interaktif melalui menu pilihan yang terus berjalan hingga pengguna memilih untuk keluar.

Struktur data yang diterapkan dalam program ini adalah Hash Map dengan metode Open Addressing untuk menangani tabrakan data. Algoritma ini bekerja dengan cara mengubah kode minuman menjadi indeks array menggunakan fungsi hash. Jika indeks yang dihasilkan sudah terisi oleh data lain, program akan mencari slot kosong berikutnya secara berurutan. Saat proses penghapusan, program menerapkan status khusus DELETED pada slot sehingga proses pencarian dan pembaruan data tetap akurat dan efisien.

C. Source Code

![alt text](<Cuplikan layar 2026-06-06 213134.png>)
![alt text](<Cuplikan layar 2026-06-06 213157.png>)
![alt text](<Cuplikan layar 2026-06-06 213234.png>)

Penjelasan kode per baris
1. Membuat kelas bernama SlotState untuk mendefinisikan status dari setiap slot di tabel hash.
2. Memberikan nilai 0 untuk status EMPTY, menandakan slot kosong dan belum diisi.
3. Memberikan nilai 1 untuk status OCCUPIED, menandakan slot sedang terisi oleh data.
4. Memberikan nilai 2 untuk status DELETED, menandakan data di slot tersebut telah dihapus.
5. -
6. Membuat kelas bernama Entry yang merepresentasikan satu slot atau elemen data di dalam tabel hash.
7. Inisialisasi konstruktor untuk kelas Entry saat objek baru dibuat.
8. Atribut untuk menyimpan kunci dari data, nilai awal adalah None.
9. Atribut untuk menyimpan nilai dari data, awalnya bernilai None.
10. Atribut untuk menyimpan status awal slot, diatur sebagai EMPTY.
11. -
12. Membuat kelas utama bernama HashMapOpenAddressing untuk mengelola struktur data hash map menggunakan metode open addressing.
13. Inisialisasi konstruktor kelas HashMapOpenAddressing dengan parameter size default 10.
14. Menyimpan ukuran kapasitas tabel hash ke dalam variabel properti self.SIZE.
15. Membuat list berisi objek-objek Entry sebanyak ukuran self.SIZE untuk menampung data.
16. -
17. Membuat fungsi hash untuk menentukan posisi indeks awal berdasarkan kunci yang dimasukkan.
18. Mengembalikan nilai indeks hasil modulo antara key dengan size tabel.
19. -
20. Membuat fungsi insert untuk memasukkan atau memperbarui data ke dalam tabel hash.
21. Mendapatkan indeks posisi awal di tabel dengan memanggil fungsi hash.
22. Melakukan perulangan pencarian slot kosong maksimal sebanyak ukuran tabel.
23. Menghitung indeks baru jika terjadi tabrakan data (collision).
24. Memeriksa apakah status slot pada indeks saat ini tidak terisi (EMPTY atau DELETED).
25. Memasukkan data kunci baru ke dalam slot tersebut.
26. Memasukkan data nilai baru ke dalam slot tersebut.
27. Mengubah status slot tersebut menjadi OCCUPIED (terisi).
28. Mengembalikan nilai True yang menandakan data berhasil dimasukkan ke dalam tabel.
29. Memeriksa apakah kunci pada slot yang terisi sama dengan kunci yang ingin dimasukkan.
30. Memperbarui nilai lama dengan nilai baru untuk kunci yang sama.
31. Mengembalikan nilai True yang menandakan data berhasil diperbarui.
32. Mengembalikan nilai False jika seluruh slot sudah penuh dan data gagal dimasukkan.
33. -
34. Membuat fungsi search untuk mencari data di dalam tabel hash berdasarkan key.
35. Mendapatkan indeks posisi awal pencarian menggunakan fungsi hash.
36. Melakukan perulangan untuk menelusuri tabel hash maksimal sebanyak ukuran tabel.
37. Menghitung indeks berikutnya yang akan diperiksa.
38. Memeriksa jika menemukan slot berstatus EMPTY.
39. Mengembalikan nilai None karena kunci data tidak ditemukan dalam tabel.
40. Memeriksa jika slot terisi dan kunci pada slot tersebut cocok dengan kunci yang dicari.
41. Mengembalikan objek slot data yang berhasil ditemukan.
42. Mengembalikan nilai None jika perulangan selesai dilakukan namun data tidak ditemukan.
43. -
44. Membuat fungsi remove_key untuk menghapus data dari tabel hash berdasarkan kuncinya.
45. Memanggil fungsi search untuk mencari keberadaan objek data yang ingin dihapus.
46. Memeriksa apakah hasil pencarian data bernilai None.
47. Mengembalikan nilai False karena proses penghapusan gagal.
48. Mengubah status slot data yang ditemukan menjadi DELETED.
49. Mengembalikan nilai True yang menandakan data berhasil dihapus.
50. -
51. Membuat fungsi display untuk menampilkan seluruh isi slot yang ada di dalam tabel hash.
52. Mencetak judul "Data Minuman:" ke layar dengan baris baru.
53. Melakukan perulangan untuk setiap indeks tabel dari awal hingga batas ukuran maksimal.
54. Mencetak nomor indeks tabel saat ini tanpa berpindah ke baris baru.
55. Memeriksa apakah status slot pada indeks tersebut adalah kosong (EMPTY).
56. Mencetak tulisan "EMPTY" untuk menandakan slot kosong.
57. Memeriksa apakah status slot pada indeks tersebut adalah terhapus (DELETED).
58. Mencetak tulisan "DELETED".
59. jika status slot adalah terisi (OCCUPIED).
60. Mencetak data berupa kunci (key) dan nilai (value) minuman yang tersimpan di slot tersebut.
61. -
62. Membuat fungsi utama main untuk menjalankan alur program.
63. Membuat objek baru dari kelas HashMapOpenAddressing dan menyimpannya di variabel hashmap.
64. Membuat perulangan tanpa batas agar menu program terus ditampilkan hingga pengguna memilih keluar.
65. Mencetak teks judul menu utama program "STOK MINUMAN".
66. Mencetak opsi menu nomor 1 untuk menambah data minuman.
67. Mencetak opsi menu nomor 2 untuk mencari data minuman.
68. Mencetak opsi menu nomor 3 untuk menghapus data minuman.
69. Mencetak opsi menu nomor 4 untuk menampilkan seluruh isi tabel.
70. Mencetak opsi menu nomor 5 untuk menghentikan program.
71. Menerima input pilihan menu dari pengguna dan menyimpannya ke variabel pilih.
72. Memeriksa apakah pengguna memilih menu nomor "1".
73. Meminta input kode minuman, mengubahnya menjadi tipe data integer, dan disimpan ke variabel kode.
74. Meminta input nama minuman berupa string dan disimpan ke variabel nama.
75. Memanggil fungsi insert untuk memasukkan data baru.
76. Mencetak pesan sukses bahwa data minuman berhasil dimasukkan.
77. Pengondisian jika fungsi insert mengembalikan nilai False.
78. Mencetak pesan peringatan bahwa tabel hash sudah penuh dan data tidak bisa masuk.
79. Memeriksa apakah pengguna memilih menu nomor "2".
80. Meminta input kode minuman yang dicari dan mengubahnya menjadi integer ke variabel kode.
81. Memanggil fungsi search dengan kunci kode dan menyimpan objek hasilnya ke variabel hasil.
82. Memeriksa apakah objek hasil ditemukan.
83. Mencetak nama minuman yang berhasil ditemukan.
84. Pengondisian jika objek hasil bernilai None.
85. Mencetak pesan bahwa data minuman tidak ada di dalam tabel.
86. Memeriksa apakah pengguna memilih menu nomor "3".
87. Meminta input kode minuman dan mengubahnya menjadi integer.
88. Memanggil fungsi remove_key untuk menghapus data.
89. Mencetak pesan sukses bahwa data minuman berhasil dihapus dari tabel.
90. Pengondisian jika fungsi remove_key mengembalikan nilai False.
91. Mencetak pesan bahwa proses hapus gagal karena data tidak ditemukan.
92. Memeriksa apakah pengguna memilih menu nomor "4".
93. Memanggil fungsi display untuk menampilkan tabel hash.
94. Memeriksa apakah pengguna memilih menu nomor "5".
95. Mencetak pesan konfirmasi bahwa program telah selesai.
96. Menghentikan paksa perulangan while True untuk keluar dari program.
97. Pengondisian jika input pilihan menu bukan 1 sampai 5.
98. Mencetak pesan bahwa pilihan yang dimasukkan pengguna salah.
99. -
100. Memeriksa apakah file script python ini dijalankan secara langsung sebagai program utama.
101. Memanggil fungsi main() untuk memulai eksekusi seluruh rangkaian program.

D. Output Program

![Ouput 1](<Cuplikan layar 2026-06-06 212149.png>)
![Output 2](<Cuplikan layar 2026-06-06 212209.png>)
![Output 3](<Cuplikan layar 2026-06-06 212223.png>)

Proses diawali dengan penambahan tiga data minuman menggunakan menu 1. Pertama, pengguna memasukkan kode 1 untuk "latte", yang berhasil ditempatkan di indeks 1 karena hasil hash-nya adalah 1. Kedua, pengguna memasukkan kode 12 untuk "matcha". Kode 12 menghasilkan indeks 2 sesuai dengan rumus fungsi hash. Ketiga, pengguna memasukkan kode 7 untuk "coffe" yang kemudian menempati indeks 7. Ketika pengguna memilih menu 4 untuk menampilkan semua data, program memperlihatkan kondisi tabel di mana indeks 1 berisi "latte", indeks 2 berisi "matcha", indeks 7 berisi "coffe", sedangkan indeks lainnya berstatus "EMPTY".

Selanjutnya, pengguna melakukan pencarian dengan menu 2 untuk mencari kode minuman 6. Namun karena slot tersebut berstatus "EMPTY" sehingga program menampilkan pesan bahwa minuman tidak ditemukan. Setelah itu, pengguna memilih menu 3 untuk menghapus data dengan kode 7. Program berhasil menemukan "coffe" di indeks 7 dan mengubah status slot tersebut menjadi "DELETED". Menu 4 dipanggil kembali untuk menampilkan seluruh data terbaru, indeks 7 yang tadinya berisi data "coffe" telah berubah menjadi "DELETED". Program diselesaikan setelah pengguna memilih menu 5 dan muncul pesan "Program selesai" dan menghentikan perulangan objek.

E. Link Youtube
link: [youtube](https://youtu.be/vt02Z0a6WvQ)
