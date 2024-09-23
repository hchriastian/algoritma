# My Algoritma Project

## Deskripsi
Proyek ini adalah implementasi dari  **Algoritma Pengurutan** untuk mengurutkan daftar angka. Anda dapat menggunakan proyek ini untuk mempelajari dasar-dasar algoritma sorting.

1. Bubble Sort https://github.com/hchriastian/algoritma/blob/main/bubble_sort.py 

*Penjelasan*:
- Iterasi: Pada setiap iterasi, elemen terbesar "mengambang" ke posisi akhir dari array yang belum terurut.
- Pengurangan Batas: Pada iterasi berikutnya, kita tidak perlu mengecek elemen terakhir karena sudah terurut.
- Efisiensi: Jika pada suatu iterasi tidak ada elemen yang ditukar, proses sorting dihentikan karena array sudah terurut. 

2. Selection Sort https://github.com/hchriastian/algoritma/blob/main/selection_sort.py

*Penjelasan*:

- Pencarian Elemen Terkecil: Pada setiap iterasi, algoritma mencari elemen terkecil di bagian array yang belum terurut (dimulai dari indeks i hingga akhir).
- Penukaran: Setelah elemen terkecil ditemukan, ia ditukar dengan elemen pertama dari bagian yang belum terurut (elemen pada indeks i).
- Pengulangan: Proses ini diulang hingga seluruh elemen terurut.

3. Insertion Sort https://github.com/hchriastian/algoritma/blob/main/insertion_sort.py

*Penjelasan*:

- Pengambilan Elemen: Algoritma mulai dari elemen kedua (indeks 1) dan menganggap elemen pertama sudah terurut.
- Perbandingan dan Pergeseran: Setiap elemen yang diambil dibandingkan dengan elemen-elemen sebelumnya. Jika elemen yang diambil lebih kecil, elemen-elemen yang lebih besar digeser ke kanan untuk memberi ruang.
- Penyisipan: Setelah menemukan posisi yang tepat, elemen disisipkan di antara elemen-elemen yang sudah terurut.


4. Shell Sort https://github.com/hchriastian/algoritma/blob/main/shell_sort.py

*Penjelasan*:

- Gap: Algoritma dimulai dengan jarak antar elemen yang besar (setengah dari panjang array) dan secara bertahap menguranginya.
- Perbandingan Elemen: Elemen yang berada sejauh "gap" dibandingkan dan dipindahkan jika tidak dalam urutan yang benar. Ini membantu "menyebarkan" elemen-elemen ke posisi yang lebih tepat lebih cepat daripada Insertion Sort.
- Kurangi Gap: Setelah seluruh elemen diproses dengan gap tertentu, gap dikurangi (biasanya menjadi setengah) dan proses diulang hingga gap menjadi 1, di mana algoritma berfungsi seperti Insertion Sort.

## Persyaratan
Sebelum menjalankan proyek ini, pastikan Anda sudah menginstall:
- Python 3.x https://learn.microsoft.com/id-id/windows/python/beginners 

## Instalasi
Clone repository ini ke dalam direktori lokal Anda dengan perintah berikut:

```bash
git clone https://github.com/hchriastian/algoritma
