A. Judul Program
PROGRAM MANAJEMEN STOK MAKANAN

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk manajemen stok makanan. Pengguna dapat menambahkan data makanan dan jumlah stoknya, melihat daftar stok yang sudah dimasukkan, dan mengedit data makanan yang ada. Program berjalan dalam loop hingga pengguna memilih untuk keluar dari program. Selain itu, program juga dilengkapi dengan validasi input untuk memastikan data yang dimasukkan sesuai dan tidak menimbulkan error.
Struktur data yang digunakan dalam program ini adalah list 1 dimensi, yaitu variabel makanan yang menyimpan kumpulan data dalam bentuk list. Setiap elemen dalam list tersebut berupa tuple (nama, stok) yang menyimpan pasangan nama makanan dan jumlah stoknya. Operasi yang dilakukan meliputi penambahan data menggunakan append, penelusuran data menggunakan perulangan for, serta pembaruan data berdasarkan indeks. 

C. Source Code
<img width="1117" height="1024" alt="Cuplikan layar 2026-04-27 081213" src="https://github.com/user-attachments/assets/293b1118-f59e-47f2-aeb3-87a472d7adc0" />
<img width="1239" height="1043" alt="Cuplikan layar 2026-04-27 081233" src="https://github.com/user-attachments/assets/b9219af0-b087-4168-82ce-b9fe93b2db32" />

Penjelasan kode per baris
1. judul program
2. -
3. membuat fungsi menu()
4. mencetak menu pertama untuk memasukkan nama dan stok makanan
5. mencetak menu kedua untuk menampilkan stok makanan
6. mencetak menu ketiga untuk edit nama dan stok makanan
7. mencetak menu keempat untuk keluar dari program
8. -
9. membuat fungsi main() sebagai program utama
10. membuat list variabel makanan = [ ] yang masih berupa list kosong
11. membuat variabel running yang bernilai boolean True agar program berjalan
12. perulangan while yang membuat program terus berjalan selama kondisi True
13. menampilkan fungsi menu()
14. program akan mencoba
15. meminta user untuk input pilihan menu yang bernilai integer
16. pengecualian jika value yang diinputkan error
17. program akan meminta user untuk memasukkan angka yang valid
18. continue berfungsi untuk membuat program kembali ke looping
19. pengondisian jika user memilih menu 1
20. program meminta user untuk input nama makanan yang akan disimpan di variabel makanan
21. perulangan saat kondisi True
22. program akan mencoba
23. meminta user untuk input stok makanan yang akan disimpan pada variabel stok
24. break berfungsi untuk mengeluarkan dari perulangan
25. pengondisian jika value yang diinputkan error
26. program akan mencetak input tidak valid dan meminta untuk memasukkan angka
27. input nama makanan dan stok makanan yang valid akan tersimpan di list makanan menggunakan operasi append
28. pengondisian jika user memilih menu 2
29. kondisi jika variabel makanan adalah list kosong
30. program mencetak “Belum ada data makanan, silakan input terlebih dahulu”
31. else, kondisi jika list makanan sudah terisi
32. program akan menampilkan stok makanan
33. mencetak garis pembatas
34. perulangan for untuk melakukan iterasi dengan operasi enumerate, nama dan stok yang ada pada list makanan
35. mencetak nomor makanan, yaitu index ditambah satu, nama makanan, dan jumlah stoknya
36. mencetak garis pembatas
37. pengondisian jika user memilih menu 3
38. kondisi jika variabel makanan adalah list kosong
39. program akan mencetak “Belum ada data makanan,silakan input terlebih dahulu”
40. else, kondisi jika list makanan sudah terisi
41. program akan mencoba
42. meminta user untuk input nomor makanan yang akan di edit dan disimpan pada variabel index
43. jika index ada di antara 0 dan jumlah karakter pada list makanan
44. program meminta user untuk input nama makanan yang baru
45. perulangan jika kondisi True
46. program akan mencoba
47. meminta user untuk input stok baru yang bernilai integer
48. break berfungsi untuk mengeluarkan dari perulangan
49. kondisi jika value yang diinputkan error
50. program mencetak “Input tidak valid, silakan masukkan angka!”
51. nama makanan dan stok makanan yang baru diedit akan terupdate di list makanan sesuai posisi indexnya
52. else, kondisi jika nomor makanan yang diinputkan user tidak ada
53. program akan mencetak nomor makanan tidak valid
54. jika value error saat user input nomor makanan
55. program mencetak “input tidak valid, silakan masukkan angka”
56. pengondisian jika user input menu 4
57. variabel running akan diubah menjadi False sehingga program berhenti
58. mencetak “program selesai”
59. kondisi jika user menginputkan selain angka 1, 2, 3 dan 4
60. program mencetak pilihan tidak valid
61. -
62. entry point, agar program hanya berjalan saat dijalankan dan jika diimport ke file lain program tidak otomatis berjalan

D. Output Program
<img width="1482" height="705" alt="Cuplikan layar 2026-04-27 085343" src="https://github.com/user-attachments/assets/5903ed7a-8989-4011-b334-6321b3ce4c30" />
<img width="1474" height="752" alt="Cuplikan layar 2026-04-27 085413" src="https://github.com/user-attachments/assets/3cb9b542-1394-4a30-b6f0-735353391f28" />

Penjelasan Output
Program akan langsung menampilkan menu saat dijalankan dan meminta user untuk menginputkan pilihan menu yang diinginkan. Saat user memilih menu 1, program meminta user untuk menginputkan nama makanan yang diisi “es krim” dan menginputkan jumlah stok makanan yang diiisi 50 oleh user. Selanjutnya, program akan melakukan perulangan dengan menampilkan menu. Selanjutnya, user memilih menu 1 lagi dengan menginputkan mie dengan stoknya yang berjumlah 100. Program akan mengulang dan menampilkan menu kembali. Tahap selanjutnya, user memilih menu 2. Program menampilkan data stok makanan yang sebelumnya sudah diinputkan oleh user. Lalu, program akan kembali ke menu dan user menginputkan menu 3. Program akan meminta user untuk menginput nomor makanan yang ingin diedit. User ingin mengedit makanan nomor 2, yaitu mie. User menginputkan nama baru makanan, yaitu mie goreng. Lalu, user mengedit jumlah stok mie goreng menjadi 70. Selanjutnya, user menginputkan menu 2 untuk menampilkan kembali data stok makanan setelah melakukan perubahan dan program pun menampilkan stok makanan yang sudah diupdate. Selanjutnya, user memilih menu 4 dan program telah selesai dijalankan.

E. Link Youtube
https://youtu.be/TB8l9Rf_noc?si=-pKb0_vl3O2b787q
