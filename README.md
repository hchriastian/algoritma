# My Algoritma Project

## Deskripsi
Proyek ini adalah implementasi dari  **Algoritma Pengurutan** untuk mengurutkan daftar angka. Anda dapat menggunakan proyek ini untuk mempelajari dasar-dasar algoritma sorting.

1. **Bubble Sort** https://github.com/hchriastian/algoritma/blob/main/bubble_sort.py 

*Penjelasan*:
- Iterasi: Pada setiap iterasi, elemen terbesar "mengambang" ke posisi akhir dari array yang belum terurut.
- Pengurangan Batas: Pada iterasi berikutnya, kita tidak perlu mengecek elemen terakhir karena sudah terurut.
- Efisiensi: Jika pada suatu iterasi tidak ada elemen yang ditukar, proses sorting dihentikan karena array sudah terurut. 

2. **Selection Sort** https://github.com/hchriastian/algoritma/blob/main/selection_sort.py

*Penjelasan*:

- Pencarian Elemen Terkecil: Pada setiap iterasi, algoritma mencari elemen terkecil di bagian array yang belum terurut (dimulai dari indeks i hingga akhir).
- Penukaran: Setelah elemen terkecil ditemukan, ia ditukar dengan elemen pertama dari bagian yang belum terurut (elemen pada indeks i).
- Pengulangan: Proses ini diulang hingga seluruh elemen terurut.

3. **Insertion Sort** https://github.com/hchriastian/algoritma/blob/main/insertion_sort.py

*Penjelasan*:

- Pengambilan Elemen: Algoritma mulai dari elemen kedua (indeks 1) dan menganggap elemen pertama sudah terurut.
- Perbandingan dan Pergeseran: Setiap elemen yang diambil dibandingkan dengan elemen-elemen sebelumnya. Jika elemen yang diambil lebih kecil, elemen-elemen yang lebih besar digeser ke kanan untuk memberi ruang.
- Penyisipan: Setelah menemukan posisi yang tepat, elemen disisipkan di antara elemen-elemen yang sudah terurut.


4. **Shell Sort** https://github.com/hchriastian/algoritma/blob/main/shell_sort.py

*Penjelasan*:

- Gap: Algoritma dimulai dengan jarak antar elemen yang besar (setengah dari panjang array) dan secara bertahap menguranginya.
- Perbandingan Elemen: Elemen yang berada sejauh "gap" dibandingkan dan dipindahkan jika tidak dalam urutan yang benar. Ini membantu "menyebarkan" elemen-elemen ke posisi yang lebih tepat lebih cepat daripada Insertion Sort.
- Kurangi Gap: Setelah seluruh elemen diproses dengan gap tertentu, gap dikurangi (biasanya menjadi setengah) dan proses diulang hingga gap menjadi 1, di mana algoritma berfungsi seperti Insertion Sort.

5. **Heap Sort** https://github.com/hchriastian/algoritma/blob/main/heap_sort.py

*Penjelasan*:

- Heapify: Sub-fungsi heapify digunakan untuk menjaga struktur max heap. Max heap adalah struktur di mana elemen terbesar selalu berada di posisi root.
- Membangun Max Heap: Array awal diubah menjadi max heap.
- Ekstraksi Elemen: Elemen terbesar (root) ditempatkan pada akhir array, kemudian heap diperbaiki (heapify) agar tetap menjadi max heap.

6. **Merge Sort** https://github.com/hchriastian/algoritma/blob/main/shell_sort.py
*Penjelasan*:

- Heapify: Sub-fungsi heapify digunakan untuk menjaga struktur max heap. Max heap adalah struktur di mana elemen terbesar selalu berada di posisi root.
- Membangun Max Heap: Array awal diubah menjadi max heap.
- Ekstraksi Elemen: Elemen terbesar (root) ditempatkan pada akhir array, kemudian heap diperbaiki (heapify) agar tetap menjadi max heap.


7. **Quick Sort menggunakan pivot** https://github.com/hchriastian/algoritma/blob/main/quick_sort_pivot.py
*Penjelasan*:

- Partitioning: Pada setiap langkah, elemen pivot dipilih (dalam contoh ini, elemen terakhir array). Semua elemen yang lebih kecil dari pivot ditempatkan di sebelah kiri pivot, dan semua elemen yang lebih besar ditempatkan di sebelah kanan.
- Rekursi: Quick Sort kemudian dijalankan secara rekursif pada sub-array di kiri dan kanan pivot, hingga semua elemen terurut.
- Base Case: Ketika low tidak lagi lebih kecil dari high, fungsi rekursif berhenti.

8. **Quick Sort menggunakan partisi** https://github.com/hchriastian/algoritma/blob/main/quick_sort_partisi.py
*Penjelasan*:

**Fungsi partition**:

- Pivot: Elemen terakhir dari array dipilih sebagai pivot.
- Partisi: Semua elemen yang lebih kecil atau sama dengan pivot dipindahkan ke sebelah kiri, dan elemen yang lebih besar dari pivot ke sebelah kanan. Pada akhir partisi, pivot ditempatkan di posisi yang benar.
- Proses ini memastikan bahwa elemen di sebelah kiri pivot lebih kecil atau sama dengan pivot, dan elemen di sebelah kanan lebih besar.

 **Fungsi quick_sort**:

- Algoritma ini memanggil fungsi partition untuk mempartisi array dan kemudian memanggil dirinya secara rekursif untuk mengurutkan bagian kiri dan kanan pivot hingga array terurut sepenuhnya.




## Persyaratan
Sebelum menjalankan proyek ini, pastikan Anda sudah menginstall:
- Python 3.x https://learn.microsoft.com/id-id/windows/python/beginners 

## Instalasi
Clone repository ini ke dalam direktori lokal Anda dengan perintah berikut:

```bash
git clone https://github.com/hchriastian/algoritma
